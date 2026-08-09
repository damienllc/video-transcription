class Exporter:
    def to_txt(self, segments, output_path: str):
        with open(output_path, "w", encoding="utf-8") as file:
            for segment in segments:
                file.write(segment.text.strip() + "\n")