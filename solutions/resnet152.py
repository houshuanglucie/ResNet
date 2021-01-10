def resnet152(num_classes, grayscale):
    """Constructs a ResNet-152 model."""
    net = ResNet(block = Bottleneck,
                 layers = [3, 8, 36, 3],
                 num_classes = num_classes,
                 grayscale = grayscale)
    return net