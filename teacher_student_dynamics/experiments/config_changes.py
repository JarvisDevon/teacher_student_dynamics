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

CONFIG_CHANGES = {
    f"learning_rate_{lr}_latent_dimension_{N}": [
{           "training": {"learning_rate": float(lr)},
            "data": {"hidden_manifold": {"latent_dimension": int(N)}},
        }
    ]
    for lr, N, in itertools.product(
       np.linspace(1.0,5.0,5),np.linspace(200,1000,9)
    )
}
