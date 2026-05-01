from parsers.resume_parser import parse_resume


def test_resume_parser():
    result = parse_resume("Python Developer")
    assert "skills" in result
