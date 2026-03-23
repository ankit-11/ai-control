from config import setup_model
from scenarios import TEST_SCENARIOS
from engine import RedTeamEngine

def main():
    print("--- Trojan-CoT Red Teaming Experiment ---")
    
    try:
        model = setup_model()
        engine = RedTeamEngine(model)
        
        engine.run(TEST_SCENARIOS)
        
        report = engine.get_report()
        print("\n" + "="*35)
        print("FINAL RESEARCH FINDINGS")
        print("="*35)
        print(f"Detection Rate (Recall): {report['recall']:.1f}%")
        print(f"False Positive Rate:     {report['fp_rate']:.1f}%")
        print(f"Total Attacks Evaded:    {report['evaded']}")
        
    except Exception as e:
        print(f"Critical Error: {e}")

if __name__ == "__main__":
    main()