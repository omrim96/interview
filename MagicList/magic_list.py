class MagicList(list):
    def __init__(self, cls_type=None):
        list.__init__(self)
        self.cls_type = cls_type

    def __setitem__(self, n, val):
        if len(self) == n:
            if self.cls_type:
                val = self.cls_type(val)
            self.append(val)
        return super(MagicList, self).__setitem__(n, val)

    def __getitem__(self, n):
        if len(self) == n and self.cls_type:
            self.append(self.cls_type())
        return super(MagicList, self).__getitem__(n)
