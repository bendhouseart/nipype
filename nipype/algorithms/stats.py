# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Managing statistical maps
"""
from __future__ import (print_function, division, unicode_literals,
                        absolute_import)
import os
import nibabel as nb
import numpy as np

from ..interfaces.base import (
    BaseInterfaceInputSpec, TraitedSpec, SimpleInterface,
    traits, InputMultiPath, File
)


class ACMInputSpec(BaseInterfaceInputSpec):
    in_files = InputMultiPath(File(exists=True), mandatory=True,
                              desc='input file, generally a list of z-stat maps')
    threshold = traits.Float(1.65, usedefault=True,
                             desc='binarization threshold. A z-value of 1.65 '
                                  'corresponds to a two-sided test of p<.10')


class ACMOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output activation count map')
    acm_pos = File(exists=True, desc='positive activation count map')
    acm_neg = File(exists=True, desc='negative activation count map')


class ACM(SimpleInterface):
    """
    Calculate a simple Activation Count Maps

    Adapted from: https://github.com/poldracklab/CNP_task_analysis/\
    blob/61c27f5992db9d8800884f8ffceb73e6957db8af/CNP_2nd_level_ACM.py
    """
    input_spec = ACMInputSpec
    output_spec = ACMOutputSpec

    def _run_interface(self, runtime):
        allmaps = nb.concat_images(
            [nb.load(f) for f in self.inputs.in_files]).get_data()
        acm_pos = (allmaps > self.inputs.threshold).astype(
            float).mean(3)
        acm_neg = (allmaps < -1.0 * self.inputs.threshold).astype(
            float).mean(3)

        acm_diff = acm_pos - acm_neg

        nii = nb.load(self.inputs.in_files[0])
        self._results['out_file'] = os.path.join(
            runtime.cwd, 'acm_diff.nii.gz')
        self._results['acm_pos'] = os.path.join(
            runtime.cwd, 'acm_pos.nii.gz')
        self._results['acm_neg'] = os.path.join(
            runtime.cwd, 'acm_neg.nii.gz')

        nb.Nifti1Image(
            acm_diff, nii.affine, nii.header).to_filename(self._results['out_file'])
        nb.Nifti1Image(
            acm_pos, nii.affine, nii.header).to_filename(self._results['acm_pos'])
        nb.Nifti1Image(
            acm_neg, nii.affine, nii.header).to_filename(self._results['acm_neg'])

        return runtime
