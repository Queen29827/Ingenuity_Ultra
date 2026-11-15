from pathlib import Path
import runpy


if __name__ == "__main__":
    game_source = Path(__file__).with_name("EndeavourForOpportunity")
    if not game_source.is_file():
        raise SystemExit(f"Game source not found: {game_source}")
    runpy.run_path(str(game_source), run_name="__main__")
