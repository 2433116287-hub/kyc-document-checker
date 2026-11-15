"""Synthetic onboarding cases and their validation rules."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Case:
    application_name: str
    id_name: str | None
    proof_of_address: str | None


@dataclass(frozen=True)
class CheckResult:
    check: str
    passed: bool
    source: str
    details: str


CASES = {
    "Complete documents": Case("Alice Tan", "Alice Tan", "Utility bill"),
    "Missing proof of address": Case("Alice Tan", "Alice Tan", None),
    "Name mismatch": Case("Alice Tan", "Alice Lim", "Utility bill"),
}


def run_checks(case: Case) -> list[CheckResult]:
    """Return the outcome and evidence for each check."""
    id_name = (case.id_name or "").strip()
    application_name = case.application_name.strip()
    address_proof = (case.proof_of_address or "").strip()
    names_match = bool(application_name and id_name) and (
        application_name.casefold() == id_name.casefold()
    )

    return [
        CheckResult(
            "Identity document present",
            bool(id_name),
            "Identity document",
            f"Name on ID: {id_name}" if id_name else "Identity document name is missing.",
        ),
        CheckResult(
            "Proof of address present",
            bool(address_proof),
            "Proof of address",
            address_proof or "Proof of address was not provided.",
        ),
        CheckResult(
            "Name matches",
            names_match,
            "Application form and identity document",
            f"Application: {application_name or 'missing'} | ID: {id_name or 'missing'}",
        ),
    ]
