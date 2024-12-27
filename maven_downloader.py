import os
import subprocess
import shutil
import sys
import re
import urllib.parse


def parse_maven_url(url):
    """
    Extracts groupId, artifactId, and version from a Maven repository URL.
    """
    try:
        parsed_url = urllib.parse.urlparse(url)
        path_parts = parsed_url.path.strip("/").split("/")
        if len(path_parts) >= 4 and path_parts[0] == "artifact":
            group_id = path_parts[1].replace("/", ".")
            artifact_id = path_parts[2]
            version = path_parts[3]
            return group_id, artifact_id, version
        else:
            raise ValueError("Invalid Maven URL format, meow! 😿")
    except Exception as e:
        print(f"Error parsing URL: {e}, nyan~! 🐾")
        return None, None, None


def create_pom_file(dependencies, output_dir):
    """
    Creates a POM file with multiple dependencies.
    """
    dependencies_xml = ""
    for group_id, artifact_id, version in dependencies:
        dependencies_xml += f"""
            <dependency>
                <groupId>{group_id}</groupId>
                <artifactId>{artifact_id}</artifactId>
                <version>{version}</version>
            </dependency>"""

    pom_content = f"""
    <project>
        <modelVersion>4.0.0</modelVersion>
        <groupId>temp</groupId>
        <artifactId>temp-artifact</artifactId>
        <version>1.0</version>
        <dependencies>
            {dependencies_xml}
        </dependencies>
    </project>
    """
    pom_path = os.path.join(output_dir, "pom.xml")
    with open(pom_path, "w") as file:
        file.write(pom_content)
    return pom_path


def download_dependencies(pom_dir):
    try:
        # Run Maven command to download dependencies 
        result = subprocess.run(
            ["mvn.cmd", "dependency:copy-dependencies", "-DoutputDirectory=dependencies"],
            cwd=pom_dir,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("Dependencies downloaded successfully, nyan~! 🎉")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error during Maven execution, meow... (＞﹏＜)")
        print(e.stderr)
        return False
    return True


def setup_local_repo_from_urls(urls, output_dir):
    if not shutil.which("mvn"):
        print("Maven is not installed or not in PATH, meow! (╥﹏╥)")
        return

    dependencies = []
    for url in urls:
        group_id, artifact_id, version = parse_maven_url(url)
        if not (group_id and artifact_id and version):
            print(f"Failed to extract artifact details from URL: {url}, nyan! (✖╭╮✖)")
            continue
        dependencies.append((group_id, artifact_id, version))

    if not dependencies:
        print("No valid dependencies to download, nyan~!")
        return

    os.makedirs(output_dir, exist_ok=True)
    pom_path = create_pom_file(dependencies, output_dir)
    print(f"POM file created at: {pom_path}, nyan~! 🐾")

    if download_dependencies(output_dir):
        print(f"Dependencies saved to: {os.path.join(output_dir, 'dependencies')}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python maven_downloader.py <maven_url1> [<maven_url2> ...]")
        sys.exit(1)

    maven_urls = sys.argv[1:]
    output_dir = "local-repo"  # You can customize the output folder here, nyan~
    
    setup_local_repo_from_urls(maven_urls, output_dir)


if __name__ == "__main__":
    main()
