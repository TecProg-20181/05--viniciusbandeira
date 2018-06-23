import pytest
from diskspace import diskspace

def test_empty_block():
    blocks = 0
    output = diskspace.bytes_to_readable(blocks)
    assert output == "0.00B"

def test_block_size():
    blocks = 1
    output = diskspace.bytes_to_readable(blocks)
    assert output == "512.00B"

def test_byte_labels():

    blocks = 2**1
    output = diskspace.bytes_to_readable(blocks)
    assert output == "1.00Kb"

    blocks = 2**11
    output = diskspace.bytes_to_readable(blocks)
    assert output == "1.00Mb"

    blocks = 2**21
    output = diskspace.bytes_to_readable(blocks)
    assert output == "1.00Gb"

    blocks = 2**31
    output = diskspace.bytes_to_readable(blocks)
    assert output == "1.00Tb"