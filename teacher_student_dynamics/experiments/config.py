from typing import Dict, List, Union

from config_manager import base_configuration

from teacher_student_dynamics import constants
from teacher_student_dynamics.experiments.config_template import ConfigTemplate


class Config(base_configuration.BaseConfiguration):
    def __init__(self, config: Union[str, Dict], changes: List[Dict] = []) -> None:
        super().__init__(
            configuration=config,
            template=ConfigTemplate.base_config_template,
            changes=changes,
        )
        self._validate_configuration()

    def _validate_configuration(self):
        """Method to check for non-trivial associations
        in the configuration.
        """
        if self.run_ode:
            assert (
                self.multi_head
            ), "ODEs currently implemented for multi-head student only."
            assert (
                self.implementation == constants.CPP
            ), "ODEs currently implemented in C++ only."
            assert (
                self.input_source == constants.IID_GAUSSIAN
            ), "ODEs implemented for IID Gaussian inputs only."
            assert (
                self.dataset_size == constants.INF
            ), "ODEs implemented for online learning (infinite dataset size) only."
            assert all(
                [not len(i) for i in self.noise_to_student_input]
            ), "ODEs implemented for noiseless inputs only."
            assert [
                i[0] == 0.0 for i in self.noise_to_teacher_output
            ], "ODEs implemented for 0-centered noise on teachers only."
            assert (
                self.train_batch_size == 1
            ), "ODEs implemented for online learning (train batch size 1) only."
            assert (
                self.optimiser == constants.SGD
            ), "ODEs implemented for SGD optimiser only."
            assert (
                self.nonlinearity == constants.SCALED_ERF
            ), "ODEs implemented for scaled error function activation only."
            assert (
                self.output_dimension == 1
            ), "ODEs implemented for regression with unit output dimension only."
            assert (
                not self.student_bias and not self.teacher_bias
            ), "ODEs implemented for networks without bias only."
            assert (
                self.interleave_period is None
            ), "Interleaved replay not implemented for ODEs."
