def resnet101(num_classes, grayscale):
    """Constructs a ResNet-101 model."""
    net = ResNet(block = Bottleneck,
                 layers = [3, 4, 23, 3],
                 num_classes = num_classes,
                 grayscale = grayscale)
    return net