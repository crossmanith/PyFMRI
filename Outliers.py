from nipype.interfaces import afni as afni
import os

data_root = 'C:/Software/PyCharm/PyFMRI/data/'
fmri_fname = data_root + 'sub-001_ses-A_task-VisStim_bold.nii.gz'
if os.path.isfile(fmri_fname):
    print('passt')
else:
    print('fail')

outlier_fname = os.path.join(data_root, 'sub-001_ses-A_task-VisStim_bold_outlier.nii.gz')
toutcount = afni.OutlierCount()
toutcount.inputs.in_file = fmri_fname
toutcount.inputs.save_outliers = True
toutcount.inputs.outliers_file = outlier_fname

res = toutcount.run()

