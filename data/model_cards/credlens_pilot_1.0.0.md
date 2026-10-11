> ⚠️ **DÉPRÉCIÉE — conservée comme trace historique.** Ces métriques ont été mesurées avec
> une fuite de données non détectée (`historical_default_rate` dérivée de la cible via
> `loan_status`, corrélation ≈0.94). Corrigé dans `credlens_pilot:1.0.1`, seule version
> à utiliser. Voir `data/model_cards/credlens_pilot_1.0.1.md`.

# Model Card — credlens_pilot
**Version** : 1.0.0 | **Type** : classification_binaire | **Algorithme** : XGBClassifier + CalibratedClassifierCV(isotonic)
**Responsable** : CredLens (contact@credlens.example)

## Usage prévu
Scoring de crédit (estimation de la probabilité de défaut) des clients d'institutions de microfinance (SFD) ; décision finale sous revue humaine (human-in-the-loop) obligatoire.

## Population cible
Clients d'institutions de microfinance (SFD) de l'UEMOA (pilot synthétique et réel).

## Métriques d'entraînement
| Métrique | Valeur |
|---|---|
| brier | 0.0700 |
| ece | 0.0210 |
| pr_auc | 0.6200 |
| roc_auc | 0.8300 |

## Seuils de décision (Policy)
| Seuil | Valeur |
|---|---|
| approve | 0.1000 |
| hard_reject | 0.5000 |
| review | 0.2500 |

## Surveillance (Monitoring)
| Alerte | Valeur |
|---|---|
| ece_max | 0.1 |
| psi_max | 0.25 |
| roc_auc_min | 0.65 |

## Limites
- Modèle entraîné sur données synthétiques pour le pilot.
- Pas de décision contractuelle sans revue humaine (REVUE_HUMAINE).
- À ré-entraîner sur les données réelles de production (protocole shadow mode).

## Considérations d'équité
Audit d'équité à reproduire sur données réelles (disparités par profil non fiabilisées sur données synthétiques).

## Sources de données
- Prototype synthétique CredLens

*Générée le 2026-08-19T13:38:14.291201+00:00.*
