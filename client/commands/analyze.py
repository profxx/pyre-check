# Copyright (c) 2016-present, Facebook, Inc.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from .. import SUCCESS, log
from .check import Check


class Analyze(Check):
    NAME = "analyze"

    def __init__(self, arguments, configuration, analysis_directory) -> None:
        super(Analyze, self).__init__(arguments, configuration, analysis_directory)

    def _flags(self):
        flags = super()._flags()
        flags.append("-analyze")
        return flags

    def _run(self, retries: int = 1) -> int:
        result = self._call_client(command=Check.NAME, flags=self._flags())
        result.check()
        log.stdout.write(result.output)

        return SUCCESS
