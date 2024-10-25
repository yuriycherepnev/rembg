from __future__ import annotations

from typing import List

from .base import BaseSession

sessions_class: List[type[BaseSession]] = []
sessions_names: List[str] = []

from .u2net import U2netSession

sessions_class.append(U2netSession)
sessions_names.append(U2netSession.name())
