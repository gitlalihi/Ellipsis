#Python program that uses 'Ellipsis' to create a multidimensional array with unspecified dimensions.
class UnspecifiedArray:
    def __getitem__(self, _):
        return UnspecifiedArray()

    def __repr__(self):
        return '...'


array_with_unspecified_dimensions = UnspecifiedArray()[..., ..., ...]
print(array_with_unspecified_dimensions)
