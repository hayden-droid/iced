# SPDX-License-Identifier: MIT
# Copyright wtfsckgh@gmail.com
# Copyright iced contributors

# ⚠️This file was generated by GENERATOR!🦹‍♂️

# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

"""
Instruction operand kind
"""

from typing import List

REGISTER: int = 0
"""
A register (:class:`iced_x86.Register`).

This operand kind uses :class:`iced_x86.Instruction.op0_register`, :class:`iced_x86.Instruction.op1_register`, :class:`iced_x86.Instruction.op2_register`, :class:`iced_x86.Instruction.op3_register` or :class:`iced_x86.Instruction.op4_register` depending on operand number. See also :class:`iced_x86.Instruction.op_register`.
"""
NEAR_BRANCH16: int = 1
"""
Near 16-bit branch. This operand kind uses :class:`iced_x86.Instruction.near_branch16`
"""
NEAR_BRANCH32: int = 2
"""
Near 32-bit branch. This operand kind uses :class:`iced_x86.Instruction.near_branch32`
"""
NEAR_BRANCH64: int = 3
"""
Near 64-bit branch. This operand kind uses :class:`iced_x86.Instruction.near_branch64`
"""
FAR_BRANCH16: int = 4
"""
Far 16-bit branch. This operand kind uses :class:`iced_x86.Instruction.far_branch16` and :class:`iced_x86.Instruction.far_branch_selector`
"""
FAR_BRANCH32: int = 5
"""
Far 32-bit branch. This operand kind uses :class:`iced_x86.Instruction.far_branch32` and :class:`iced_x86.Instruction.far_branch_selector`
"""
IMMEDIATE8: int = 6
"""
8-bit constant. This operand kind uses :class:`iced_x86.Instruction.immediate8`
"""
IMMEDIATE8_2ND: int = 7
"""
8-bit constant used by the ``ENTER``, ``EXTRQ``, ``INSERTQ`` instructions. This operand kind uses :class:`iced_x86.Instruction.immediate8_2nd`
"""
IMMEDIATE16: int = 8
"""
16-bit constant. This operand kind uses :class:`iced_x86.Instruction.immediate16`
"""
IMMEDIATE32: int = 9
"""
32-bit constant. This operand kind uses :class:`iced_x86.Instruction.immediate32`
"""
IMMEDIATE64: int = 10
"""
64-bit constant. This operand kind uses :class:`iced_x86.Instruction.immediate64`
"""
IMMEDIATE8TO16: int = 11
"""
An 8-bit value sign extended to 16 bits. This operand kind uses :class:`iced_x86.Instruction.immediate8to16`
"""
IMMEDIATE8TO32: int = 12
"""
An 8-bit value sign extended to 32 bits. This operand kind uses :class:`iced_x86.Instruction.immediate8to32`
"""
IMMEDIATE8TO64: int = 13
"""
An 8-bit value sign extended to 64 bits. This operand kind uses :class:`iced_x86.Instruction.immediate8to64`
"""
IMMEDIATE32TO64: int = 14
"""
A 32-bit value sign extended to 64 bits. This operand kind uses :class:`iced_x86.Instruction.immediate32to64`
"""
MEMORY_SEG_SI: int = 15
"""
``seg:[SI]``. This operand kind uses :class:`iced_x86.Instruction.memory_size`, :class:`iced_x86.Instruction.memory_segment`, :class:`iced_x86.Instruction.segment_prefix`
"""
MEMORY_SEG_ESI: int = 16
"""
``seg:[ESI]``. This operand kind uses :class:`iced_x86.Instruction.memory_size`, :class:`iced_x86.Instruction.memory_segment`, :class:`iced_x86.Instruction.segment_prefix`
"""
MEMORY_SEG_RSI: int = 17
"""
``seg:[RSI]``. This operand kind uses :class:`iced_x86.Instruction.memory_size`, :class:`iced_x86.Instruction.memory_segment`, :class:`iced_x86.Instruction.segment_prefix`
"""
MEMORY_SEG_DI: int = 18
"""
``seg:[DI]``. This operand kind uses :class:`iced_x86.Instruction.memory_size`, :class:`iced_x86.Instruction.memory_segment`, :class:`iced_x86.Instruction.segment_prefix`
"""
MEMORY_SEG_EDI: int = 19
"""
``seg:[EDI]``. This operand kind uses :class:`iced_x86.Instruction.memory_size`, :class:`iced_x86.Instruction.memory_segment`, :class:`iced_x86.Instruction.segment_prefix`
"""
MEMORY_SEG_RDI: int = 20
"""
``seg:[RDI]``. This operand kind uses :class:`iced_x86.Instruction.memory_size`, :class:`iced_x86.Instruction.memory_segment`, :class:`iced_x86.Instruction.segment_prefix`
"""
MEMORY_ESDI: int = 21
"""
``ES:[DI]``. This operand kind uses :class:`iced_x86.Instruction.memory_size`
"""
MEMORY_ESEDI: int = 22
"""
``ES:[EDI]``. This operand kind uses :class:`iced_x86.Instruction.memory_size`
"""
MEMORY_ESRDI: int = 23
"""
``ES:[RDI]``. This operand kind uses :class:`iced_x86.Instruction.memory_size`
"""
MEMORY: int = 25
"""
Memory operand.

This operand kind uses :class:`iced_x86.Instruction.memory_displ_size`, :class:`iced_x86.Instruction.memory_size`, :class:`iced_x86.Instruction.memory_index_scale`, :class:`iced_x86.Instruction.memory_displacement`, :class:`iced_x86.Instruction.memory_base`, :class:`iced_x86.Instruction.memory_index`, :class:`iced_x86.Instruction.memory_segment`, :class:`iced_x86.Instruction.segment_prefix`
"""

__all__: List[str] = []
