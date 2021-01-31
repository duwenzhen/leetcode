class SnapshotArray:

    def __init__(self, length: int):
        self.dicohelp = {}
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        self.dicohelp[index] = val

    def snap(self) -> int:
        self.snaps.append(self.dicohelp.copy())
        return len(self.snaps) - 1


    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id][index] if index in self.snaps[snap_id] else 0

snapshotArr = SnapshotArray(3)

snapshotArr.set(0,5)
snapshotArr.snap()
snapshotArr.set(0,6)
print(snapshotArr.get(0,0))