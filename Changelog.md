# Changelog
All notable changes to this project will be documented in this file

[unreleased]: https://github.com/eugenesvk/xontrib-mise/compare/0.0.4...HEAD
## [Unreleased]
<!-- - __Added__ -->
  <!-- + :sparkles:  -->
  <!-- new features -->
<!-- - __Changed__ -->
  <!-- +   -->
  <!-- changes in existing functionality -->
<!-- - __Fixed__ -->
  <!-- + :beetle:  -->
  <!-- bug fixes -->
<!-- - __Deprecated__ -->
  <!-- + :poop:  -->
  <!-- soon-to-be removed features -->
<!-- - __Removed__ -->
  <!-- + :wastebasket:  -->
  <!-- now removed features -->
<!-- - __Security__ -->
  <!-- + :lock:  -->
  <!-- vulnerabilities -->

[0.0.4]: https://github.com/eugenesvk/xontrib-mise/releases/tag/0.0.4
## [0.0.4]
  - __Changed__
    + drop trying to find a binary in a nonexistent cache, which is now very costly, especially with larger `$PATH`s

[0.0.3]: https://github.com/eugenesvk/xontrib-mise/releases/tag/0.0.3
## [0.0.3]
  - __Changed__
    + renamed `rtx.py` to `mise.py` to avoid confusion in loading

[0.0.2]: https://github.com/eugenesvk/xontrib-mise/releases/tag/0.0.2
## [0.0.2]
  - __Changed__
    + renamed `rtx` to `mise` (though continue to check for both binaries)
