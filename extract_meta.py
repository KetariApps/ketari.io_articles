import os
import frontmatter
import ruamel.yaml


def combine_files():
    data = {}

    # Get a list of all markdown files in the "articles" directory
    for filename in os.listdir("./articles"):
        if filename.endswith(".md"):
            file_path = os.path.join("./articles", filename)

            with open(file_path) as f:

                # Use frontmatter to extract the YAML data from the file
                metadata, content = frontmatter.parse(f.read())

                # Add the YAML data to the "data" dictionary
                data[filename] = metadata
    

    # Write the combined data to data.yml
    with open("./data.yml", "w") as f:
        yaml = ruamel.yaml.YAML()
        yaml.dump(data, f)

if __name__ == "__main__":
    combine_files()
