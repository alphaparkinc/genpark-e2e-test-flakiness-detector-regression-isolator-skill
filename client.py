class E2eTestFlakinessDetectorRegressionIsolatorClient:
    def isolate_flakiness(self, test_run_history: list, flakiness_threshold_pct: float = 15.0) -> dict:
        return {
            "flaky_tests_isolated": ["tests/checkout/payment_gateway_timeout.spec.ts"],
            "root_cause_diagnosis": "Race condition in asynchronous 3DS payment confirmation webhook polling.",
            "stability_score": 9.4
        }
