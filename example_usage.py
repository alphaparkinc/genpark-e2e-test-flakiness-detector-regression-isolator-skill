from client import E2eTestFlakinessDetectorRegressionIsolatorClient

def main():
    client = E2eTestFlakinessDetectorRegressionIsolatorClient()
    history = [{"run_id": "r1", "pass": True}, {"run_id": "r2", "pass": False}, {"run_id": "r3", "pass": True}]
    res = client.isolate_flakiness(history)
    print(f"Stability Score: {res['stability_score']}/10")
    print("Flaky Tests:", res["flaky_tests_isolated"])
    print(f"Diagnosis: {res['root_cause_diagnosis']}")

if __name__ == "__main__":
    main()
