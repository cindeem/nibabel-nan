import nibabel
import numpy as np


if __name__ == '__main__':

    infile = 'rdata_with_nan.nii'
    img = nibabel.load(infile)
    affine = img.get_affine()
    dat = img.get_data().copy()
    fixed = np.nan_to_num(dat)
    newimg = nibabel.Nifti1Image(fixed, affine)
    
