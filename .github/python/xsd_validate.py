import argparse
import os
import xmlschema

def validate_xml_files(xsd_path, xml_dir):
    """Validates XML files in a directory against a given XSD schema."""
    schema = xmlschema.XMLSchema(xsd_path)
    at_least_one_invalid = False
    for filename in os.listdir(xml_dir):
        if filename.endswith(".xml"):
            xml_path = os.path.join(xml_dir, filename)
            try:
                schema.validate(xml_path)
                print(f"✅ {filename} is valid")
            except xmlschema.XMLSchemaValidationError as e:
                print(f"❌ {filename} is NOT valid:\n{e}")
                at_least_one_invalid = True
    
    if at_least_one_invalid:
        os._exit(1)

def main():
    parser = argparse.ArgumentParser(description="Validate XML files against an XSD schema.")
    parser.add_argument("-xsd_file", help="Path to the XSD schema file")
    parser.add_argument("-xml_directory", help="Directory containing XML files to validate")
    args = parser.parse_args()

    validate_xml_files(args.xsd_file, args.xml_directory)

if __name__ == "__main__":
    main()
