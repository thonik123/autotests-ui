import pytest

@pytest.mark.xfail(reason="найжен быг, из-за него тест падает")
def test_with_bug():
    assert 1==2

@pytest.mark.xfail(reason="буг уже исправлен, но маркировка Хфейл ещё висит на нём")
def test_without_bug():
    ...