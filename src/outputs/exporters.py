thonpython
import json
import logging

class JSONExporter:
    def export(self, data, path):
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            logging.info(f"Exported JSON to {path}")
        except Exception as e:
            logging.error(f"Error exporting JSON: {e}")