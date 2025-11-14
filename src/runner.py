thonpython
import json
import logging
from pathlib import Path
from extractors.rumble_video_parser import RumbleVideoParser
from extractors.rumble_channel_parser import RumbleChannelParser
from outputs.exporters import JSONExporter
from extractors.utils_helpers import detect_input_type

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def main():
    data_path = Path(__file__).resolve().parent.parent / "data" / "input.sample.json"
    settings_path = Path(__file__).resolve().parent / "config" / "settings.example.json"

    with open(settings_path, "r", encoding="utf-8") as f:
        settings = json.load(f)

    with open(data_path, "r", encoding="utf-8") as f:
        inputs = json.load(f)

    exporter = JSONExporter()

    results = []

    for item in inputs.get("queries", []):
        logging.info(f"Processing: {item}")
        input_type = detect_input_type(item)

        if input_type == "video":
            parser = RumbleVideoParser(settings)
            results.append(parser.parse(item))
        elif input_type == "channel":
            parser = RumbleChannelParser(settings)
            results.append(parser.parse(item))
        else:
            logging.warning(f"Unknown input type for: {item}")

    output_path = Path(__file__).resolve().parent.parent / "data" / "sample_output.json"
    exporter.export(results, output_path)

    logging.info(f"Completed. Output saved to {output_path}")

if __name__ == "__main__":
    main()