import platform

import pytest

from tinyvdiff_demo.fpdf2 import generate_pdf_single_page, generate_pdf_multi_page, data

skip_if_not_linux = pytest.mark.skipif(
    platform.system() != "Linux", reason="Visual regression tests only run on Linux"
)


@pytest.fixture
def temp_pdf(tmp_path):
    """Fixture to create a temporary PDF file path"""
    return tmp_path / "test.pdf"


@skip_if_not_linux
def test_fpdf2_single_page_visual(tinyvdiff, temp_pdf):
    """Test visual regression with single-page PDF generated with fpdf2"""
    pdf_path = generate_pdf_single_page(data, temp_pdf)
    tinyvdiff.assert_pdf_snapshot(pdf_path, "snapshot_fpdf2_single.svg")


@skip_if_not_linux
def test_fpdf2_multi_page_visual(tinyvdiff, temp_pdf):
    """Test visual regression with multi-page PDF generated with fpdf2"""
    pdf_path = generate_pdf_multi_page(temp_pdf, num_pages=3)
    tinyvdiff.assert_pdf_snapshot(pdf_path, "snapshot_fpdf2_multi.svg")
