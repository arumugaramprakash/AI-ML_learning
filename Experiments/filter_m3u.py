#!/usr/bin/env python3
"""
Script to filter an .m3u file based on hardcoded keywords while preserving complete structure.
Creates a subset .m3u containing only relevant entries, maintaining all metadata and formatting.
"""

import sys
import urllib.request

def filter_m3u(input_file, output_file):
    """Filter m3u file with full structure preservation."""
    keywords = ["tamil","vijay", "sun ", "raj ", "kid", "toon", "cartoon", "pogo", "animal", "discovery", "national"]  # Original set of keywords
    is_extended = False
    in_extinf_block = False
    extinf_lines = []
    block_matches = False

    try:
        # Try multiple encodings if utf-8 fails
        for encoding in ['utf-8', 'latin-1']:
            try:
                with open(input_file, 'r', encoding=encoding) as infile, \
                     open(output_file, 'w', encoding='utf-8') as outfile:

                    # Write header (first line)
                    header = infile.readline()
                    if '#EXTM3U' in header:
                        is_extended = True
                    outfile.write(header)

                    for line in infile:
                        stripped_line = line.strip()

                        # Handle extended m3u format blocks
                        if is_extended and stripped_line.startswith('#EXTINF:'):
                            extinf_lines.append(line)
                            in_extinf_block = True
                            block_matches = any(keyword.lower() in stripped_line.lower()
                                               for keyword in keywords)
                            continue

                        if in_extinf_block:
                            extinf_lines.append(line)

                            # Check if this line contains a URL (ends with .m3u8 or http/https)
                            if any(stripped_line.endswith(ext) for ext in ['.m3u8', '.mp4']):
                                # Only write block if it matches keywords
                                if block_matches:
                                    outfile.writelines(extinf_lines)
                                extinf_lines = []
                                in_extinf_block = False

                        # Also check non-EXTINF lines for keywords (for simple m3u format)
                        elif not in_extinf_block and any(keyword.lower() in stripped_line.lower()
                                                         or keyword.lower() in line.lower()
                                                         for keyword in keywords):
                            outfile.write(line)

                    print(f"Successfully filtered {input_file} to {output_file}")
                    return True
            except UnicodeDecodeError:
                continue

        raise Exception("All encoding attempts failed")

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return False

def fetch_remote_file(url):
    """Fetch content from a URL and return as string."""
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8', errors='replace')
    except Exception as e:
        # print(f"Error fetching remote file: {e}", file=sys.stderr)
        return None

# ... existing code remains the same until the if __name__ == "__main__": block ...

if __name__ == "__main__":
    # Handle command line arguments or default to local file
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "filtered_output.m3u"
    else:
        # input_file = "TV_List.m3u"  # Default to your local file
        input_file = "https://iptv-org.github.io/iptv/index.m3u"
        output_file = "filtered_TV.m3u"

    try:
        # Check if input is a URL or local file
        if input_file.startswith(('http://', 'https://')):
            content = fetch_remote_file(input_file)
            if not content:
                print(f"Failed to fetch remote file: {input_file}", file=sys.stderr)
                sys.exit(1)

            # Write to temporary file with UTF-8 encoding
            import tempfile
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False, suffix='.m3u') as tmp:
                tmp.write(content)
                input_file = tmp.name

        if not filter_m3u(input_file, output_file):
            sys.exit(1)

    finally:
        # Clean up temporary file only for URLs
        if 'input_file' in locals() and any(input_file.startswith(prefix) for prefix in ('http://', 'https://')):
            import os
            try:
                os.unlink(input_file)
            except:
                pass

    print(f"Filtering complete. Output saved to: {output_file}")