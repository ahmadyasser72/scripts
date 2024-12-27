# Scripts

This repository contains a collection of random scripts I have written. Each script serves a specific purpose, and the repository will grow over time as I add more utilities.

## Current Scripts

### 1. `maven_downloader.py`

#### Description
A Python script to download Maven dependencies from URLs. This tool helps you set up a local Maven repository by parsing Maven URLs and creating a `pom.xml` file to fetch the specified dependencies.

#### Usage
```bash
python maven_downloader.py <maven_url1> [<maven_url2> ...]
```

- Replace `<maven_url1>`, `<maven_url2>` with actual Maven artifact URLs.
- Dependencies will be downloaded to the `local-repo/dependencies` directory.

#### Example
```bash
python maven_downloader.py https://repo.maven.apache.org/maven2/com/google/guava/guava/31.1-jre
```

#### Requirements
- Python 3.x
- Maven installed and available in the system's PATH.

---

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

