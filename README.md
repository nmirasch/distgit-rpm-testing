# distgit-rpm-testing

A dist-git repository for RPM package generation.

## Overview

This repository follows the dist-git structure used by Fedora and similar distributions for managing RPM packages. It contains the necessary files to build an RPM package using tools like `rpmbuild` or `mock`.

## Repository Structure

- `example-package.spec` - RPM spec file containing package metadata and build instructions
- `sources` - File containing checksums of source archives (lookaside cache references)
- `.gitignore` - Excludes build artifacts from version control

## Building the RPM

### Prerequisites

- Install RPM build tools:
  ```bash
  # On Fedora/RHEL/CentOS
  sudo dnf install rpm-build rpmdevtools
  
  # On Ubuntu/Debian
  sudo apt-get install rpm
  ```

### Build Instructions

1. Set up the RPM build environment:
   ```bash
   rpmdev-setuptree
   ```

2. Copy the spec file and source tarball:
   ```bash
   cp example-package.spec ~/rpmbuild/SPECS/
   cp example-package-1.0.0.tar.gz ~/rpmbuild/SOURCES/
   ```

3. Build the RPM:
   ```bash
   rpmbuild -ba ~/rpmbuild/SPECS/example-package.spec
   ```

4. The built RPM will be available in `~/rpmbuild/RPMS/noarch/`

### Using Mock (recommended for clean builds)

```bash
mock -r fedora-39-x86_64 --rebuild example-package-1.0.0-1.src.rpm
```

## Files Explained

### Spec File (`example-package.spec`)

The spec file contains all the metadata and instructions for building the RPM:
- Package name, version, and release
- Dependencies
- Build and installation instructions
- List of files to be packaged
- Changelog

### Sources File

The `sources` file contains SHA512 checksums of source archives. In production dist-git repositories (like those used by Fedora), large source files are stored in a "lookaside cache" and referenced by their checksums. This keeps the git repository small.

## Customization

To adapt this for your own package:

1. Rename `example-package.spec` to match your package name
2. Update the spec file with your package details
3. Create your source tarball and update the `sources` file with its checksum
4. Commit the changes to git

## Resources

- [RPM Packaging Guide](https://rpm-packaging-guide.github.io/)
- [Fedora Packaging Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/)
- [dist-git Documentation](https://github.com/release-engineering/dist-git)
