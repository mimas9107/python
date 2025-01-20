import os
from skimage import io, color, exposure
import matplotlib.pyplot as plt
import numpy as np

BLU = 0
GRN = 1
RED = 2
GRY = 3
PUBLIC_DATASET_FOLDER = 'dataset'

def get_image_filenames(folder=PUBLIC_DATASET_FOLDER, short=False):
    '''
      Parameter:
        folder specifies a folder name containing the image dataset, a string
            short specifies whether the returned filenames are full-path (by
            default) or short filenames, a boolean.
      Returns:
        img_filenames specifies a list of image filenames, a list.
      Does:
        Collect all the image filenames under the specified folder.
    '''

    img_filenames = []
    for root, _, files in os.walk(folder):
        for f in files:
            f = f.lower()
            if f.endswith('.jpg') or f.endswith('.jpeg'):
                if not short:
                    img_path = os.path.join(root, f)
                    img_filenames.append(img_path)
                else:
                    img_filenames.append(f)
    return img_filenames

def get_image_histograms(img_filenames, channel=RED, normalize=True):
    '''
      Parameter:
        img_filenames specifies a list of image filenames, a list.
        channel specifies which color channel or gray scale is applied to form
            the histogram, an integer.
        normalize specifies whether the frequency of the returned histogram is
            normalized to [0, 1] (by default) or not, a boolean.
      Returns:
        hists stores histograms in a dictionary, in which each key and value
            pair corresponds to a pair of an image filename and its histogram,
            a dict.
      Does:
        Collect all the histograms for each image filename according to the
            specific color channel or gray scale.
    '''
    # Dictionary to store histograms
    hists = {}
    for img_filename in img_filenames:
        print(img_filename)
        # Read image
        img = io.imread(img_filename)

        # Calculate histogram
        if channel == RED:
            hist = exposure.histogram(img[:,:,RED], normalize=normalize)[0]
        elif channel == GRN:
            hist = exposure.histogram(img[:,:,GRN], normalize=normalize)[0]
        elif channel == BLU:
            hist = exposure.histogram(img[:,:,BLU], normalize=normalize)[0]
        else:
            # Convert to grayscale
            img_gray = color.rgb2gray(img)
            hist = exposure.histogram(img_gray, normalize=normalize)[0]

        # Save histogram
        hists[img_filename] = hist
    return hists

def get_image_statistics(img_filenames, channel=RED):
    '''
      Parameter:
        img_filenames specifies a list of image filenames, a list.
        channel specifies which color channel or gray scale is applied to
            calculate the image statistics (including mean, standard
            deviation, and variance), an integer.
      Returns:
        stats stores image statistics in a dictionary, in which each key and
            value pair corresponds to a pair of an image filename and its
            histogram, a dict.
      Does:
        Collect all the image statistics for each image filename according to
            the specific color channel or gray scale.
    '''
    # Dictionary to store histograms
    stats = {}
    for img_filename in img_filenames:
        # Read image
        img = io.imread(img_filename)

        stat = np.zeros((3, 1))
        # Calculate histogram
        if channel == RED:
            stat[0] = np.mean(img[:,:,RED])
            stat[1] = np.var(img[:,:,RED])
            stat[2] = np.std(img[:,:,RED])
        elif channel == GRN:
            stat[0] = np.mean(img[:,:,GRN])
            stat[1] = np.var(img[:,:,GRN])
            stat[2] = np.std(img[:,:,GRN])
        elif channel == BLU:
            stat[0] = np.mean(img[:,:,BLU])
            stat[1] = np.var(img[:,:,BLU])
            stat[2] = np.std(img[:,:,BLU])
        else:
            # Convert to grayscale
            img_gray = color.rgb2gray(img)
            stat[0] = np.mean(img_gray)
            stat[1] = np.var(img_gray)
            stat[2] = np.std(img_gray)

        # Save statistics
        stats[img_filename] = stat
    return stats

def get_sim_matrix(img_filenames, features, normalize=True, round=True):
    '''
      Parameter:
        img_filenames specifies a list of image filenames, a list.
        features specifies a dictionary of image features, where each key
            and value pair corresponds to a pair of an image filename and
            its feature, a dict.
        normalize specifies whether the similarity matrix is normalized to
            [0, 1] (by default) or not, a boolean.
        round specifies whether the entries in the similarity matrix are
            rounded (by default) or not, a boolean.
      Returns:
        sim_matrix stores a similarity matrix, in which each entry at position
            (i, j) is computed as the Euclidean distance between the image
            feature i and the image feature j, a numpy.
      Does:
        Compute a similarity matrix based on the procedure described below.
            For each entry located at (i, j) in the matrix, we first get the
            filenames of the images i and j. The corresponding features i and j
            of the two images are obtained through access to the dictionary
            features. Next, we compute their feature similarity based on the
            definition of Euclidean distance. As a result, the larger value of
            the matrix entry's value indicates the less similarity between the
            two images in terms of the specific feature representations.
            According to the above process, it is obvious that the matrix is
            symmetric since the distance between images i and j is the same
            as the distance between images j and i.
    '''
    # Calculate all pairwise similarities
    num_images = len(features)
    sim_matrix = np.zeros((num_images, num_images))

    for i in range(num_images):
        for j in range(i, num_images):
            if j > i:
                feature_i = features[img_filenames[i]]
                feature_j = features[img_filenames[j]]

                # Measure histogram distance based on Euclidean distance
                if feature_j.size == feature_i.size:
                    sim = np.linalg.norm(feature_i - feature_j)
                    sim_matrix[i, j] = sim
                    sim_matrix[j, i] = sim
    if normalize:
        sim_matrix = (sim_matrix-np.min(sim_matrix))/(np.max(sim_matrix)-np.min(sim_matrix))
    if round:
        sim_matrix = np.round(sim_matrix, 4)

    return sim_matrix

def vis_sim_matrix(sim_matrix, keys_short, title='Image Similarity Matrix', filename=None):
    '''
      Parameter:
        sim_matrix specifies a similarity matrix, a numpy.
        keys_short specifies a list of image filenames in short format,a list.
        title specifies the title of the plot of the similarity matrix, a
            string. By default, title='Image Similarity Matrix.'
        filename specifies the filename to store the plot as an image, a string.
            By default, filename=None indicates no need to store the plot as an
            image.
      Returns:
        None.
      Does:
        Visualize the similarity matrix based on the procedure described below.
            Regarding the similarity matrix as 2D scalar data, we invoke the
            function imshow, provided by matplotlib, to render a (default)
            pseudocolor image, in which a darker pseudocolor indicates much
            similarity, while a lighter pseudocolor corresponds to less
            similarity. In addition, when rendering the image, for each entry
            located at (i, j) in the matrix, its similarity value is also
            used to for annotation. As for axes' labels, the short version
            of image filename is used to label ticks for both horizontal and
            vertical axes. To plot the image in compact format,  we rotate
            the labels of the horizontal axis by 45 degrees.
    '''
    # Visualize similarity matrix
    fig, ax = plt.subplots(figsize=(50, 50))
    im = ax.imshow(sim_matrix)

    # Label axes
    ax.set_xticks(np.arange(len(keys_short)), labels=keys_short)
    ax.set_yticks(np.arange(len(keys_short)), labels=keys_short)

    # Rotate labels
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Annotate matrix values
    for i in range(len(keys_short)):
        for j in range(len(keys_short)):
            ax.text(j, i, sim_matrix[i, j], ha="center", va="center", color="w")

    ax.set_title(title)
    fig.tight_layout()
    if filename is not None:
        plt.savefig(filename)
    plt.show()

def vis_image_stats(filename):
    '''
      Parameter:
        filename specifies the full-path filename of an image, a string.
      Returns:
        None.
      Does:
        Read the image file and split into red, green, blue, and gray-scale
        channels. For each channel, we do the followings:
        1. Calculate image statistics, including mean, standard deviation,
            and variance;
        2. Extract image histogram;
        3. Generate a plot that contains two sub-plots. The left-hand side
            sub-plot shows the image histogram, in which the x-axis indicates
            the random variable with gray-scale range [0, 255] and the y-axis
            indicates the frequency of a random variable (i.e., the number
            of pixels). The right-hand side, on the other hand, sub-plot
            utilizes the box plot to display minimum, first quartile, median,
            third quartile, and maximum of values in intensity range [0, 255].
            In the title of the box plot, the image statistics are annoated as
            well.
    '''
    img = io.imread(filename)
    # Split RGB channels
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    hist_r = exposure.histogram(r, normalize=False)[0]
    hist_g = exposure.histogram(g, normalize=False)[0]
    hist_b = exposure.histogram(b, normalize=False)[0]
    # Convert to grayscale
    gray = color.rgb2gray(img) * 255
    hist_gray = exposure.histogram(gray, normalize=False)[0]

    # Calculate statistics
    r_mean = np.mean(r)
    r_var = np.var(r)
    r_std = np.std(r)

    g_mean = np.mean(g)
    g_var = np.var(g)
    g_std = np.std(g)

    b_mean = np.mean(b)
    b_var = np.var(b)
    b_std = np.std(b)

    gray_mean = np.mean(gray)
    gray_var = np.var(gray)
    gray_std = np.std(gray)

    # Plot histogram
    plt.subplot(1, 2, 1)
    plt.plot(hist_r)
    plt.xlabel('intensity value')
    plt.ylabel('number of pixels')
    plt.title('Red channel')
    plt.subplot(1, 2, 2)
    plt.boxplot(r.ravel())
    plt.xticks([])
    plt.xlabel('red')
    plt.ylabel('intensity value')
    plt.title('Mean: %.2f, Var: %.2f\nSTD: %.2f' % (r_mean, r_var, r_std))
    plt.tight_layout()
    plt.show()

    plt.subplot(1, 2, 1)
    plt.plot(hist_g)
    plt.xlabel('intensity value')
    plt.ylabel('number of pixels')
    plt.title('Green channel')
    plt.subplot(1, 2, 2)
    plt.boxplot(g.ravel())
    plt.xticks([])
    plt.xlabel('green')
    plt.ylabel('intensity value')
    plt.title('Mean: %.2f, Var: %.2f\nSTD: %.2f' % (g_mean, g_var, g_std))
    plt.tight_layout()
    plt.show()

    plt.subplot(1, 2, 1)
    plt.plot(hist_b)
    plt.xlabel('intensity value')
    plt.ylabel('number of pixels')
    plt.title('Blue channel')
    plt.subplot(1, 2, 2)
    plt.boxplot(b.ravel())
    plt.xticks([])
    plt.xlabel('blue')
    plt.ylabel('intensity value')
    plt.title('Mean: %.2f, Var: %.2f\nSTD: %.2f' % (b_mean, b_var, b_std))
    plt.tight_layout()
    plt.show()

    plt.subplot(1, 2, 1)
    plt.plot(hist_gray)
    plt.xlabel('intensity value')
    plt.ylabel('number of pixels')
    plt.title('Grayscale')
    plt.subplot(1, 2, 2)
    plt.boxplot(gray.ravel())
    plt.xticks([])
    plt.xlabel('gray scale')
    plt.ylabel('intensity value')
    plt.title('Mean: %.2f, Var: %.2f\nSTD: %.2f' % (gray_mean, gray_var, gray_std))
    plt.tight_layout()
    plt.show()

def vis_image(filename):
    '''
      Parameter:
        filename specifies the full-path filename of an image, a string.
      Returns:
        None.
      Does:
        Read the image file and split into red, green, blue, and gray-scale
        channels. For each channel, we call the function imshow, provided by
        matplotlib, to render a color image with the color on its own.
    '''
    img = io.imread(filename)
    # Split RGB channels
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    # Convert to grayscale
    gray = color.rgb2gray(img)

    # Plot images
    plt.imshow(r, cmap='Reds')
    plt.title('Red channel')
    plt.xlabel('width')
    plt.ylabel('height')
    plt.show()

    plt.imshow(g, cmap='Greens')
    plt.title('Green channel')
    plt.xlabel('width')
    plt.ylabel('height')
    plt.show()

    plt.imshow(b, cmap='Blues')
    plt.title('Blue channel')
    plt.xlabel('width')
    plt.ylabel('height')
    plt.show()

    plt.imshow(gray, cmap='gray')
    plt.title('Grayscale')
    plt.xlabel('width')
    plt.ylabel('height')
    plt.show()

def main():
    keys = get_image_filenames(PUBLIC_DATASET_FOLDER)
    keys_short = get_image_filenames(PUBLIC_DATASET_FOLDER, short=True)

    hists = get_image_histograms(keys, RED)
    sim_matrix = get_sim_matrix(keys, hists)
    vis_sim_matrix(sim_matrix, keys_short, filename='sim_matrix_red.png')

    hists = get_image_histograms(keys, GRN)
    sim_matrix = get_sim_matrix(keys, hists)
    vis_sim_matrix(sim_matrix, keys_short, filename='sim_matrix_green.png')

    hists = get_image_histograms(keys, BLU)
    sim_matrix = get_sim_matrix(keys, hists)
    vis_sim_matrix(sim_matrix, keys_short, filename='sim_matrix_blue.png')

    hists = get_image_histograms(keys, GRY)
    sim_matrix = get_sim_matrix(keys, hists)
    vis_sim_matrix(sim_matrix, keys_short, filename='sim_matrix_gray.png')

    stats = get_image_statistics(keys, RED)
    sim_matrix = get_sim_matrix(keys, stats)
    vis_sim_matrix(sim_matrix, keys_short, filename='sim_matrix_stats_red.png')

    stats = get_image_statistics(keys, GRN)
    sim_matrix = get_sim_matrix(keys, stats)
    vis_sim_matrix(sim_matrix, keys_short, filename='sim_matrix_stats_green.png')

    stats = get_image_statistics(keys, BLU)
    sim_matrix = get_sim_matrix(keys, stats)
    vis_sim_matrix(sim_matrix, keys_short, filename='sim_matrix_stats_blue.png')

    stats = get_image_statistics(keys, GRY)
    sim_matrix = get_sim_matrix(keys, stats)
    vis_sim_matrix(sim_matrix, keys_short, filename='sim_matrix_stats_gray.png')

    i = 29
    img_filename = keys[i]
    vis_image(img_filename)
    vis_image_stats(img_filename)

if __name__ == '__main__':
    main()