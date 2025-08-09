def test_secure_blocks_dangerous_command():
    from core import secure_mode
    dangerous = "rm -rf /"
    safe = "ls -la"

    assert not secure_mode.is_safe_command(dangerous)
    assert secure_mode.is_safe_command(safe)
