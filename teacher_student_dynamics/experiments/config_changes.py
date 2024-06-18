import itertools
import numpy as np

#param_config_changes = {
#    f"param_{h}": [{"networks": {"student_hidden": h, "teacher_hidden": h}}]
#    for h in [1, 2, 4]
#}
#oparam_config_changes = {
#    f"oparam_{h}": [{"networks": {"student_hidden": 2 * h, "teacher_hidden": h}}]
#    for h in [1, 2, 4]
#}
#CONFIG_CHANGES = {**param_config_changes, **oparam_config_changes}

#CONFIG_CHANGES = {
#    f"latent_dimension_{a}": [
#{           "data": {"hidden_manifold": {"latent_dimension": int(a)}},
#        }
#    ]
#    for a in np.linspace(400,800,10)
#}

CONFIG_CHANGES = {
    f"feature_rotation_alpha_{a}": [
{           "networks": {"rotation_teachers": {"feature_rotation_alpha": float(a)}},
        }
    ]
    for a in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
}
