class Model():
    def __init__(self, mtype, dataset):
        self.mtype = mtype
        self.dataset = dataset
        self.list_all()

    def list_all(self):
        print(
            'Mode type: {:20s} - Dataset: {:20s}'.format(self.mtype, self.dataset.data_type))


class Dataset():
    def __init__(self):
        self.data_type = self.make()

    def make(self):
        return "Raw"


class Coco(Dataset):
    def __init__(self):
        super(Coco, self).__init__()

    def make(self):
        return self.__class__.__name__


class VOC(Dataset):
    def __init__(self):
        super(VOC, self).__init__()

    def make(self):
        return self.__class__.__name__


if __name__ == "__main__":
    d = Dataset()
    c = Coco()
    v = VOC()
    m1 = Model('YOLO', d)
    m2 = Model('YOLO', c)
    m3 = Model('YOLO', v)
    # Output:
    # Mode type: YOLO                 - Dataset: Raw
    # Mode type: YOLO                 - Dataset: Coco
    # Mode type: YOLO                 - Dataset: VOC
