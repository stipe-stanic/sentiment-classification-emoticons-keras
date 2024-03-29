import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


def plot_single_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.show()


# 2 x 3 images
def show_images_from_set(dataset, class_names):
    plt.figure(figsize=(10, 10))
    for images, labels in dataset.take(1):
        for i in range(6):
            ax = plt.subplot(2, 3, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(class_names[labels[i]])
            plt.axis("off")
    plt.show(block=False)


# 3 x 3 images
def show_augmented_images_from_set(dataset, augmentation_fn):
    plt.figure(figsize=(10, 10))
    for images, _ in dataset.take(1):
        for i in range(9):
            augmented_images = augmentation_fn(images)
            ax = plt.subplot(3, 3, i + 1)
            plt.imshow(augmented_images[0].numpy().astype("uint8"))
            plt.axis("off")
    plt.show(block=False)


def plot_model_metrics(epochs_range, acc, val_acc, loss, val_loss):
    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc="lower right")
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc="upper right")
    plt.title('Training and Validation Loss')
    plt.show(block=False)


def plot_confusion_matrix(y_test, y_pred, class_names):
    fig, ax = plt.subplots(figsize=(10, 10))
    ConfusionMatrixDisplay.from_predictions(y_test, y_pred, display_labels=class_names, xticks_rotation="vertical",
                                            ax=ax, colorbar=False)
    plt.show(block=False)
