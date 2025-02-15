import numpy as np
import matplotlib.pyplot as plt

def convolve(x, h):
    """
    Convolves two sequences x and h.
    
    Parameters:
    x (numpy array): First sequence (usually the input signal)
    h (numpy array): Second sequence (usually the impulse response or kernel)
    
    Returns:
    numpy array: The convolved result
    """
    # Compute the convolution using np.convolve
    y = np.convolve(x, h, mode='full')
    return y

# Example usage
if __name__ == "__main__":
    # Define two sequences x and h
    x = np.array([1, 2, 3])
    h = np.array([4, 5, 6])
    
    # Perform convolution
    y = convolve(x, h)
    
    print("Input sequence x:", x)
    print("Impulse response (kernel) h:", h)
    print("Convolved result y:", y)
    
    # Plotting the sequences and their convolution
    plt.figure(figsize=(10, 6))
    
    plt.subplot(3, 1, 1)
    plt.plot(x, marker='o')
    plt.title('Input Sequence x')
    
    plt.subplot(3, 1, 2)
    plt.plot(h, marker='s')
    plt.title('Impulse Response (Kernel) h')
    
    plt.subplot(3, 1, 3)
    plt.plot(y, marker='x')
    plt.title('Convolved Result y')

    plt.tight_layout()
    plt.show()