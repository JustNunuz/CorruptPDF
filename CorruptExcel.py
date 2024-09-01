import os
import zipfile
import xml.dom.minidom
import xml.etree.ElementTree as ET
from pathlib import Path

def corrupt_excel_file(input_path, output_path):
    # Backup the original file
    input_path.rename(Path(str(input_path) + '_backup'))

    # Load the xlsx as a zip archive
    with zipfile.ZipFile(input_path, 'r') as zip_ref:
        zip_ref.extractall('.')

        # Find the sheets
        sheets = {}
        for member in zip_ref.namelist():
            if '/xl/worksheets/' in member:
                sheet_name = member[:-len('/content.xml')]
                sheets[sheet_name] = {'xml': member, 'rows': []}

    # Parse the XML files for each sheet
    for sheet_name, attrs in sheets.items():
        dom = xml.dom.minidom.parse(attrs['xml'])

        # Traverse nodes
        rows = []
        for row_node in traverse(dom.childNodes):
            if isinstance(row_node, ET.ElementBase) and row_node.tag == "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row":
                rows.append(row_node)

        attrs['rows'] = rows

    # Switch rows
    for row_node in sheets:
        rows = sheets[row_node]['rows'][::-1]
        temp = ET.Element('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheetData', attrib={'r:Id': 'rId{}'.format(row_node[-1:])})
        for row in rows:
            temp.append(row)

        # Save the modified XML
        with open(sheets[row_node]['xml'], 'wb') as f:
            f.write(ET.tostring(temp, encoding='utf-8', xml_declaration=True).decode('utf-8'))

    # Repack the corrupted Excel file
    repacked_zip = zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk('./'):
        for file in files:
            if not file.startswith('~$') and not file.startswith('~TEMP'):
                repacked_zip.write(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file)))

    repacked_zip.close()

    # Delete the extracted files
    for folderName, _, fileNameList in os.walk('./'):
        for file_name in fileNameList:
            if not file_name.startswith('~$') and not file_name.startswith('~TEMP'):
                os.remove(os.path.join(folderName, file_name))
                os.rmdir(folderName)

def traverse(nodes):
    """Traverse Node Iterator"""
    for node in nodes:
        if node.nodeType == node.ELEMENT_NODE:
            yield node
        if node.hasChildNodes():
            for childNode in traverse(node.childNodes):
                yield childNode

input_path = Path('test.xlsx')
output_path = Path('corrupted_test.xlsx')

corrupt_excel_file(input_path, output_path)