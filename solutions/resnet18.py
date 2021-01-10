def resnet18(num_classes, grayscale):
    """Constructs a ResNet-18 model."""
    net = ResNet(block = BasicBlock,
                 layers = [2, 2, 2, 2],
                 num_classes = num_classes,
                 grayscale = grayscale)
    return net