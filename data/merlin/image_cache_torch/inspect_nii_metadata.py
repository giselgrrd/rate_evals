import os
import nibabel as nib
import numpy as np

root = r'/root/rate-evals/data/merlin/image_cache_torch/'
files = [f for f in os.listdir(root) if f.endswith('.nii') or f.endswith('.nii.gz')]
if not files:
    raise FileNotFoundError('No NIfTI files found in ' + root)
path = os.path.join(root, files[0])
img = nib.load(path)
hdr = img.header
data = img.get_fdata(dtype=np.float32)
print('found', files)
print('path', path)
print('shape', data.shape)
print('dtype', data.dtype)
print('min', float(np.nanmin(data)))
print('max', float(np.nanmax(data)))
print('affine', img.affine)
print('zooms', hdr.get_zooms())
print('data_dtype', hdr.get_data_dtype())
print('dim_info', hdr['dim_info'])
descrip = hdr['descrip'].item()
print('descrip', descrip.decode('utf-8','ignore') if isinstance(descrip, bytes) else descrip)
print('pixdim', hdr['pixdim'])
print('qform_code', hdr['qform_code'], 'sform_code', hdr['sform_code'])
print('qoffset', hdr['qoffset_x'], hdr['qoffset_y'], hdr['qoffset_z'])
print('srow_x', hdr['srow_x'])
print('srow_y', hdr['srow_y'])
print('srow_z', hdr['srow_z'])