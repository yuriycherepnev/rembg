from typing import List

import numpy as np
from PIL import Image
from scipy.special import log_softmax

from .session_base import BaseSession

# fmt: off
pallete1 = [
      0,   0,   0, # background
    255, 255, 255, # upper body
      0,   0,   0, # lower body
      0,   0,   0, # full body
]

pallete2 = [
      0,   0,   0, # background
      0,   0,   0, # upper body
    255, 255, 255, # lower body
      0,   0,   0, # full body
]

pallete3 = [
      0,   0,   0, # background
      0,   0,   0, # upper body
      0,   0,   0, # lower body
    255, 255, 255, # full body
]
# fmt: on


class ClothSession(BaseSession):
    def predict(self, img: Image) -> List[Image]:
        ort_outs = self.inner_session.run(
            None, self.normalize(img, (0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (768, 768))
        )

        pred = ort_outs
        pred = log_softmax(pred[0], 1)
        pred = np.argmax(pred, axis=1, keepdims=True)
        pred = np.squeeze(pred, 0)
        pred = np.squeeze(pred, 0)

        mask = Image.fromarray(pred.astype("uint8"), mode="L")
        mask = mask.resize(img.size, Image.LANCZOS)

        masks = []

        mask1 = mask.copy()
        mask1.putpalette(pallete1)
        mask1 = mask1.convert("RGB").convert("L")
        masks.append(mask1)

        mask2 = mask.copy()
        mask2.putpalette(pallete2)
        mask2 = mask2.convert("RGB").convert("L")
        masks.append(mask2)

        mask3 = mask.copy()
        mask3.putpalette(pallete3)
        mask3 = mask3.convert("RGB").convert("L")
        masks.append(mask3)

        return masks
