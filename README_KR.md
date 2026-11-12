# iOS 27 A17 Pro 탈옥 추적기

**iPhone 15 Pro Max**(Apple A17 Pro, 기기 식별자 `iPhone16,2`)의 **iOS 27.0.1**(빌드 `24A446`)에 관한 독립 연구 및 호환성 추적 저장소입니다.

> **현재 상태(2026-11-12 기준 데이터): NO-GO. 대상 기기 준비도 LEVEL 0.** 이 기기와 빌드에 대해 검증된 탈옥은 아직 없습니다. 이 저장소는 탈옥 도구가 아니며, 익스플로잇 코드, 도구, 설치 절차를 제공하지 않습니다.

## 1. 프로젝트 소개

이 저장소는 iOS 27.0.1(빌드 24A446)의 iPhone 15 Pro Max 탈옥 연구에 관한 공개 정보를 수집하고, 검증하고, 점수화합니다. 독립적인 연구 및 호환성 프로젝트이며, Apple, Calif.io, Hexacon, Dopamine 프로젝트와 제휴 관계가 없습니다.

모든 주장은 출처, 날짜, 적용 범위, 판정, 한계와 함께 기록합니다. 언론 보도에만 근거한 내용은 "보도됨(reported)"으로 표시합니다. 커뮤니티 주장은 1차 출처가 확인하기 전까지 단서로만 취급합니다.

**AI 보조 사용 공개.** 초안 작성과 연구 보조는 Anthropic이 만든 AI 모델 Claude가 수행했습니다. 관리자가 결과를 검토하며, 모든 주장에는 출처가 있습니다. Apple의 iOS 27 보안 공지는 두 개의 CVE 항목에서 Calif.io와 함께 "Claude and Anthropic Research"를 명시합니다(C-006). 이 프로젝트는 Apple의 표현을 그대로 인용할 뿐, 그 협업 방식에 대해 추론하지 않습니다. 이 프로젝트는 관리자가 독립적으로 운영하며, Anthropic의 제품이 아닙니다.

## 2. 프로젝트 목표

- 대상 기기와 빌드에 대해 탈옥 경로가 존재하는지 근거로 확정합니다.
- 탈옥으로 이어질 수 있는 연구 영역을 추적합니다: SPTM, 커널 연구, 샌드박스 탈출과 권한 상승, 빌드 호환성, 익스플로잇 체인 통합, 탈옥 생태계, 지속성, 사기 탐지.
- 실제 기기를 연구 위험으로부터 보호합니다. 이 프로젝트는 관리자가 소유한 기기에 연결하거나, 검사하거나, 수정하지 않으며, 실제 기기에 대한 작업을 권하지 않습니다.
- 펌웨어 사실관계를 정확하게 유지합니다: 설치된 빌드, 서명 상태, 알려지지 않은 사항.
- 다른 사람들이 확인, 정정, 재사용할 수 있도록 근거를 공개합니다(19절의 라이선스).

## 3. 대상 하드웨어

이 저장소는 iOS 27.0.1(빌드 24A446)을 실행하는 iPhone 15 Pro Max(A17 Pro)에 대한 독립적인 연구 대상 프로필을 관리합니다.

이 대상 프로필은 호환성 연구에 사용됩니다. 저장소 관리자의 개인 기기 상태를 공개하거나 검증하지 않습니다.

이 프로젝트는 관리자가 소유한 기기에 연결하거나, 검사하거나, 수정하지 않습니다.

| 항목 | 값 |
|---|---|
| 제품 | iPhone 15 Pro Max |
| 기기 식별자 | `iPhone16,2`(제3자 색인; C-025) |
| 칩셋 | Apple A17 Pro(C-026, 부분 검증) |
| 아키텍처 | arm64 |

다섯 단계의 근거 수준과 아직 확정되지 않은 수준은 [docs/DEVICE_PROFILE.md](docs/DEVICE_PROFILE.md)에 있습니다.

## 4. 대상 펌웨어

| 항목 | 값 |
|---|---|
| iOS 버전 | 27.0.1, 2026-09-28 출시(C-024) |
| 빌드 | 24A446(제3자 색인; C-003, 부분 검증) |
| Apple 보안 공지 | 27.0.1에 공개된 CVE 항목 없음(C-007) |
| 서명 상태(공개 관찰) | 미해결. 제3자 펌웨어 색인 ipsw.me(S-014)는 빌드 24A446을 서명되지 않음으로 나열하며, 2026-11-12에 마지막으로 확인했습니다. 커뮤니티 참고 자료(S-026)는 2026-11-02에 서명됨으로 보고했으므로, 관찰 시점 사이에 상태가 바뀌었습니다. 변경 날짜는 알려지지 않았습니다(C-021, E-030). Apple은 프로젝트가 확인할 수 있는 서명 기록을 공개하지 않았습니다. |

연구 대상은 iOS 27.0.1(빌드 24A446)로 고정되어 있습니다(위의 대상 프로필 참조). 이 절의 펌웨어 관찰은 공개 출처에서 가져왔으며, 출처와 마지막 확인 날짜를 함께 적었습니다.

## 5. 연구 현황

**데이터 스냅샷(2026-11-12):** 주장 106건(검증됨 62, 부분 검증 24, 미검증 20), 출처 46건, 타임라인 사건 32건, 호환성 행 15건, 펌웨어 빌드 4건.

**현재 위치: 대상 기기 LEVEL 0.** Calif.io가 2026-10-16에 iPhone 18 Pro(A20 Pro)에서 iOS 27.0.1 untethered 탈옥을 시연했다고 보도되었습니다(C-001, 부분 검증). 그 시연은 대상 기기를 사용하지 않았습니다. 검증된 기술 문서나 도구는 없습니다. Dopamine 3.0 릴리스 노트는 실기기 SPTM 지원이 iOS 17.3.1에서 끝난다고 명시합니다(C-066). A17 Pro에 대한 iOS 27 지원은 문서화되어 있지 않습니다(C-018). 이번 v0.2.0 연구 업데이트는 Apple의 iOS 27.2 및 27.2.1 공지를 매핑하고([apple-27x-cve-mapping.md](research/apple-27x-cve-mapping.md)), 상류 참고 자료를 주장별로 대조합니다([upstream-reconciliation.md](research/upstream-reconciliation.md)). 준비도 수준은 바뀌지 않았습니다.

영역별 연구 현황(세부 내용은 [research/](research/)):

| 영역 | 상태 |
|---|---|
| DIM01 사건 검증 | 부분 연구 |
| DIM02 A17 Pro 아키텍처 | 부분 연구 |
| DIM03 SPTM 연구 | 연구됨(등급화 감사: [sptm-evidence-audit.md](research/sptm-evidence-audit.md)) |
| DIM04 커널 취약점 정보 | 연구됨(Apple 공지 매핑: [apple-27x-cve-mapping.md](research/apple-27x-cve-mapping.md)) |
| DIM05 샌드박스 탈출 및 권한 상승 | 부분 연구(Apple 공지 텍스트만) |
| DIM06 펌웨어 및 빌드 호환성 | 부분 연구 |
| DIM07 익스플로잇 체인 통합 | 부분 연구 |
| DIM08 탈옥 생태계 | 부분 연구 |
| DIM09 지속성 및 배포 | 부분 연구 |
| DIM10 사기 탐지 | 부분 연구 |
| DIM11 일상 사용 안정성 | 평가되지 않음 |
| DIM12 복구 및 안전 | 부분 연구 |

## 6. 호환성 대시보드

상태 기준: `verified`(검증됨), `partially_verified`(부분 검증), `reported_unverified`(보도됨, 미검증), `unverified`(미검증), `not_established`(대상에 대한 검증된 근거 없음), `not_researched`(미연구).

| ID | 분류 | 상태 | 근거 | 비고 |
|---|---|---|---|---|
| CMP-001 | SPTM Research | 부분 검증 | C-013, C-014 | Apple defines SPTM for A15-or-later SoCs, which includes the A17 Pro by ordering. |
| CMP-002 | SPTM Bypass | 미검증 | C-015 | The only SPTM bypass mention is a community reference describing an undisclosed bypass. |
| CMP-003 | Kernel Vulnerability | 미검증 | C-037, C-039, C-041, C-070, C-071 | Apple's iOS 27 and iOS 27.2 notes list kernel-memory write and corruption entries (research/apple-27x-cve-mapping.md). |
| CMP-004 | Kernel Read | 미검증 | C-035, C-040 | Apple lists kernel-memory read, disclosure and layout impacts: eight on the iOS 27 page (including CVE-2026-84622, which needs root) and six on the iOS 27.2 page. |
| CMP-005 | Kernel Write | 미검증 | C-037, C-039, C-041 | Apple lists write and corruption impacts for kernel memory on the iOS 27 and iOS 27.2 pages. |
| CMP-006 | Sandbox Escape | 확정되지 않음 | C-034, C-048, C-074 | Apple lists a WebContent sandbox escape reachable by a remote attacker (iOS 27.2: CVE-2026-112690) and a WebKit Process Model escape (iOS 27.2: CVE-2026-113897). |
| CMP-007 | Privilege Escalation | 확정되지 않음 | C-035, C-036, C-074 | Apple lists a kernel entry in which a malicious app may gain root privileges (iOS 27: CVE-2026-43689) and an entry in which an app with root privileges reads uninitialised kernel memory (iOS 27: CVE-2026-84622). |
| CMP-008 | AMFI Compatibility | 미연구 | - | AMFI (code signing enforcement) was not researched in this pass. |
| CMP-009 | Complete Exploit Chain | 보도됨, 미검증 | C-001, C-002, C-027, C-038, C-042, C-049 | A complete chain is reported only for an iPhone 18 Pro (A20 Pro) demonstration. |
| CMP-010 | Bootstrap | 확정되지 않음 | C-016, C-055, C-065, C-066 | No bootstrap for iOS 27.0.1 is verified. |
| CMP-011 | Package Manager | 확정되지 않음 | C-030, C-056, C-057 | Sileo's latest release is 2.5.1 (2024-10-08), with no iOS 27 mention (C-030). |
| CMP-012 | Persistence | 보도됨, 미검증 | C-004, C-053 | Reboot persistence is reported for the iPhone 18 Pro demonstration (C-004). |
| CMP-013 | Public Jailbreak Tool | 확정되지 않음 | C-028, C-058, C-064 | No publicly installable tool is verified for this target (C-028). |
| CMP-014 | Independent A17 Pro Reproduction | 확정되지 않음 | C-049, C-062 | No independent reproduction on A17 Pro hardware was found. |
| CMP-015 | Exact Build Verification | 부분 검증 | C-003, C-024, C-025, C-078, C-079 | Build 24A446 for iPhone16,2 is corroborated by third-party sources and by the Apple index date. |

모든 행은 대상 프로필(iPhone16,2, A17 Pro, iOS 27.0.1, 빌드 24A446)에 맞춰 적용됩니다. `not_established`는 해당 행에 검증된 근거가 없다는 뜻이며, 답이 "아니오"라는 뜻이 아닙니다.

## 7. SPTM 연구

- Apple은 SPTM이 A15 이상 및 M2 이상 SoC에서 지원되며, 지원되는 플랫폼에서 PPL을 대체한다고 밝혔습니다(C-013). A17 Pro는 이 범주에 속합니다(C-014, 부분 검증).
- 대상 A17 Pro에 대한 공개 SPTM 우회는 검증되지 않았습니다. 커뮤니티 참고 자료는 iOS 27.0.1까지 유효한 SPTM 우회를 보고하며, 27.2 베타에서 패치되었다고 합니다. 1차 게시물은 확인하지 못했습니다(C-051, 미검증).
- Dopamine 3.0 릴리스 노트는 iOS 17.4 이상에 알려진 SPTM 우회가 없어서 실기기 SPTM 지원이 iOS 17.3.1에서 끝난다고 명시합니다(C-066). 같은 노트의 Titan 우회는 iOS 16.5.1~17.3.1을 다룹니다(C-065).
- 독립 SPTM 논문은 iOS 18.4의 iPhone 16을 분석하며, A17 Pro나 iOS 27 빌드는 다루지 않습니다(C-060).

세부 내용: [research/sptm-evidence-audit.md](research/sptm-evidence-audit.md)와 [research/DIM03-sptm-research.md](research/DIM03-sptm-research.md).

## 8. 커널 연구

- Apple의 iOS 27 보안 공지는 Calif.io 연구자를 CVE-2026-65409, CVE-2026-65410, CVE-2026-28968, CVE-2026-86886 네 개 항목에 대해 인정합니다(C-038). 이 가운데 CVE-2026-28968은 커널 메모리 손상 영향을 가진 Kernel 항목입니다.
- Apple의 iOS 27.2 보안 공지는 Calif.io 연구자를 여섯 개 항목에 대해 인정합니다. 어느 것도 커널 메모리 영향을 갖지 않습니다(C-042).
- Apple의 iOS 27.2 공지는 커널 메모리 항목 23개를 나열합니다: 쓰기 4, 손상 12, copy-on-write 1, 읽기 또는 노출 6. 공지는 영향받는 버전 범위를 밝히지 않습니다(C-039~C-041, C-047).
- Apple 색인은 27.0.1에 공개된 CVE 항목이 없다고 나열합니다(C-007).
- 커널 읽기/쓰기 공개가 2026-11-04에 예고되었습니다. 2026-11-12 기준 공개물은 찾지 못했습니다(C-022, C-049).
- 대상에 대해 검증된 공개 커널 익스플로잇은 없습니다.

세부 내용: [research/DIM04-kernel-vulnerability.md](research/DIM04-kernel-vulnerability.md)와 [research/apple-27x-cve-mapping.md](research/apple-27x-cve-mapping.md).

## 9. 익스플로잇 체인 현황

- 보고된 유일한 완전한 체인은 iPhone 18 Pro(A20 Pro)에서 시연되었습니다. 기술 문서는 공개되지 않았고 구성 요소도 공개되지 않았습니다(C-001, C-027).
- 대상 기기에 대해 검증된 완전한 체인은 없습니다. 준비도: LEVEL 0.
- 이 프로젝트는 익스플로잇 코드를 공개하거나, 실행하거나, 설명하지 않습니다.

세부 내용: [research/DIM07-exploit-chain.md](research/DIM07-exploit-chain.md).

## 10. 탈옥 생태계

- **Dopamine:** 최신 공식 릴리스는 3.0.13(2026-11-03, C-017)입니다. 3.0.2~3.0.13 릴리스 노트는 iOS 27을 언급하지 않습니다(C-055). 3.0 릴리스는 실기기 SPTM 지원이 iOS 17.3.1에서 끝난다고 명시합니다(C-066). A17 Pro에 대한 iOS 27 지원은 문서화되어 있지 않습니다(C-018).
- **Sileo:** Sileo/Sileo 저장소의 최신 릴리스는 2.5.1(2024-10-08)입니다. 릴리스 노트는 iOS 27을 언급하지 않습니다(C-030, 부분 검증).
- **ElleKit:** 이전 저장소 식별자는 GitHub 릴리스가 없는 저장소로 리디렉션됩니다(C-056). 상류 자료의 "ElleKit 1.2가 iOS 27을 포함한다"는 주장은 미검증입니다(C-057).
- **프로젝트 공지:** 2026년 11월 iOS 27.0~27.0.1 대상 프로젝트 주장은 미검증이며 위험도가 높습니다(C-064). 이번 점검에서 릴리스는 검토하지 않았습니다.
- **BootROM 문제:** A12 및 A13 칩에 대해 보고되었으며, A17 Pro는 해당하지 않습니다(C-019, 부분 검증).

세부 내용: [research/DIM08-jailbreak-ecosystem.md](research/DIM08-jailbreak-ecosystem.md).

## 11. 일상 사용 준비도

**평가되지 않음.** 대상에 대해 검증된 탈옥이 없으므로, 안정성, 배터리, Face ID, 뱅킹 및 인증 앱, 그 밖의 일상 사용 항목을 평가할 근거가 없습니다. LEVEL 6에 도달하지 않았습니다. 세부 내용: [research/DIM11-daily-driver-stability.md](research/DIM11-daily-driver-stability.md).

## 12. 펌웨어 보존

| 버전 | 빌드 | 출시일 | 서명 상태(기록) | Apple CVE 상태 |
|---|---|---|---|---|
| 27.0 | 24A437 | 2026-09-14 | 서명 안 됨(제3자 색인), 2026-11-12 | Apple 페이지에 나열됨 |
| 27.0.1 | 24A446 | 2026-09-28 | 서명 안 됨(제3자 색인), 2026-11-12 | 공개 없음 |
| 27.2 | 24B119 | 2026-10-26 | 서명됨(제3자 색인), 2026-11-12 | Apple 페이지에 나열됨 |
| 27.2.1 | 24B156 | 2026-11-09 | 서명됨(제3자 색인), 2026-11-12 | Apple 페이지에 나열됨 |

- 설치된 빌드는 복원 가능한 빌드와 같지 않습니다. 복원은 복원 시점의 Apple 서명에 달려 있습니다.
- 24A446의 서명 상태는 미해결입니다. 제3자 색인 ipsw.me(S-014)는 2026-11-12 확인 기준 서명되지 않음으로 나열하며, 커뮤니티 참고 자료(S-026)는 2026-11-02에 서명됨으로 보고했습니다. 그 사이에 상태가 바뀌었습니다(C-021, E-030). 이 빌드로의 복원이 가능하다고 가정하지 마십시오.
- SHSH blob은 복원을 보장하지 않습니다.
- 이 프로젝트는 업데이트나 다운그레이드를 권하지 않습니다. 그 결정은 기기 소유자의 몫입니다.
- 업데이트 지연 설정은 기기가 제공하는 경우에도 모든 업데이트 또는 복원 경로를 막는다고 보장하지 않습니다. 적용 범위는 기기와 버전에 따라 다르며, 이 프로젝트는 이를 검증하지 않습니다.
- 어떤 기기에서든 실험 실패나 복구 시도가 더 새로운 펌웨어 설치로 이어질 수 있으며, 그러면 해당 빌드는 일반 경로로 복원할 수 없게 될 수 있습니다. 이 프로젝트는 그런 위험을 수반하는 작업을 권하지 않습니다.

세부 내용: [docs/RECOVERY_AND_PRESERVATION.md](docs/RECOVERY_AND_PRESERVATION.md)와 [reports/firmware-report.md](reports/firmware-report.md).

## 13. 연구 타임라인

| 날짜 | 사건 | 검증 상태 | 출처 |
|---|---|---|---|
| 2025-09 | Apple announces Memory Integrity Enforcement with the iPhone 17 and iPhone Air, naming the A19 and A19 Pro chips. | 검증됨 | S-003 |
| 2025-10-10 | Independent academic analysis of SPTM, TXM and Exclaves (arXiv:2510.09272) is submitted. Its firmware analysis uses iPhone 16 (A18) on iOS 18.4, not the A17 Pro or iOS 27. | 검증됨 | S-035 |
| 2026-06-18 | usbliter8 BootROM exploit for A12 and A13 devices is publicised (reported by secondary outlets and a national CERT). | 부분 검증 | S-021, S-022, S-023 |
| 2026-08-07 | Dopamine 3.0 released; secondary coverage quotes a support table of iOS 15.0 to 17.3.1 for A8 to A17 and M1 to M2, and iOS 26.0 to 26.0.1 for A12 and A13. | 부분 검증 | S-009 |
| 2026-08-07 | Dopamine 3.0 release notes state a Titan PPL/SPTM bypass for iOS 16.5.1 to 17.3.1, a momentarius PPL bypass for A12 and A13, and that real-device SPTM support ends at iOS 17.3.1 because no bypass is known for 17.4 and later. | 검증됨 | S-007 |
| 2026-09-14 | iOS 27.0 released (build 24A437 per the third-party index). | 부분 검증 | S-014, S-001 |
| 2026-09-21 | Press reports Apple stopped signing iOS 26.6.2 after iOS 27 shipped. Used as a pattern example for how older builds lose signing. | 부분 검증 | S-020 |
| 2026-09-28 | iOS 27.0.1 released (build 24A446). Apple's security releases index lists no published CVE entries for this build. | 부분 검증 | S-002, S-014, S-016 |
| 2026-10-16 | Calif.io reportedly demonstrates an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro at Hexacon 2026 in Paris. | 부분 검증 | S-010, S-011, S-012 |
| 2026-10-17 | An opa334 PSA dated 2026-10-17 is reported by the upstream reference to warn of an SPTM bypass valid through iOS 27.0.1. The original was not located in this review. | 미검증 | S-026 |
| 2026-10-19 | Apple's iOS 27 security notes are updated with CVE entries credited to Calif.io researchers, two of them jointly with Claude and Anthropic Research. | 검증됨 | S-001 |
| 2026-10-19 | The upstream reference reports a Calif.io team member's interview on end-user tools, the scope of the chain and a 27.2 patch statement. The interview was not retrieved. | 미검증 | S-026 |
| 2026-10-23 | Apple's index lists iOS 27.1 for iPhone Duo with no published CVE entries. | 검증됨 | S-002 |
| 2026-10-26 | iOS 27.2 released (build 24B119 per the third-party index). Secondary press reports 163 fixed vulnerabilities; Apple's 27.2 advisory was not located. | 부분 검증 | S-002, S-014, S-017, S-018 |
| 2026-10-26 | Apple's iOS 27 security page is updated with entries marked as added on 2026-10-26, including CVE-2026-112608 (CoreMedia) and CVE-2026-86916 (kernel privilege impact). | 검증됨 | S-001 |
| 2026-10-30 | A Calif.io social account reportedly posted a bare hash without explanation (upstream reference). The content it commits to is unknown. | 미검증 | S-026 |
| 2026-10-30 | A company-branded account reportedly showed a root shell on iOS 27.2 (upstream reference). Single-party, unverified (C-063). | 미검증 | S-026 |
| 2026-11-01 | A project announced a semi-untethered iOS 27.0 to 27.0.1 jailbreak with a planned release one to two weeks later (upstream reference). The upstream reference found no proof of concept or third-party validation. No release was reviewed in this pass. Any future release should be treated as potentially malicious (C-064). | 미검증 | S-026 |
| 2026-11-02 | A community reference states that iOS 27.0.1 was still signed on 2026-11-02. This is not independently verified and conflicts with the third-party index checked on 2026-11-11. | 미검증 | S-026 |
| 2026-11-03 | Dopamine 3.0.13 published. Release notes describe a posix_spawn hook fix and a SpringBoard snapshot change. They do not state iOS 27 support. | 검증됨 | S-007 |
| 2026-11-03 | Press reports that Apple responded to MIE-bypass claims with an iOS update. Details were not verified. | 미검증 | S-024 |
| 2026-11-04 | Reported plan for a kernel read/write exploit and write-up from a Calif.io-linked researcher within about a week. Coverage conflicts; no primary announcement was located. | 미검증 | S-026, S-029 |
| 2026-11-04 | Reported (upstream reference, V31): opa334 says Dopamine A12 and A13 support could follow using momentarius once a kernel read/write exploit is public; A14 and later still need an SPTM bypass. Original not retrieved. | 미검증 | S-026 |
| 2026-11-04 | Reported (upstream reference, V32): a Calif.io video shows Lockdown Mode, an over-the-air update to iOS 27.2, and a reboot after which a plugin still works. Video and original post not retrieved. | 미검증 | S-026 |
| 2026-11-06 | Press coverage through about 2026-11-06 reports that Apple fixed most flaws in iOS 27.2 and that no public tool is planned. | 부분 검증 | S-019 |
| 2026-11-09 | iOS 27.2.1 released (build 24B156 per the third-party index and the Wikipedia infobox). | 부분 검증 | S-002, S-014, S-030 |
| 2026-11-11 | Tracker snapshot. The third-party index lists iOS 27.0.1 as not signed. A community reference reports the opposite for 2026-11-02, so the status is unresolved. | 부분 검증 | S-014, S-026 |
| 2026-11-11 | The one-week window reported on 2026-11-04 for a kernel read/write write-up lapses. No publication, repository or source-code release for the announced work was found on 2026-11-12. | 부분 검증 | S-029, S-013 |
| 2026-11-12 | Research pass for the v0.2.0 update: Apple's iOS 27.2 and 27.2.1 advisories parsed, the upstream reference reconciled, and the kernel, Calif.io and SPTM evidence re-classified. | 검증됨 | S-033, S-034, S-026 |
| 2026-11-12 | The third-party index lists iOS 27.0.1 (24A446) as not signed on 2026-11-12. The upstream reference recorded it as signed on 2026-11-02. The date of the change is not known (C-021). | 부분 검증 | S-014, S-026 |
| 2026-11-12 | Local static provenance and Ghidra analysis of the 24A446 kernelcache and the SPTM and TXM monitor images. Manifest digests match the normal containers; restore-entry digests do not match (unresolved). The complete package was not hashed. Readiness is unchanged. | 부분 검증 | S-043 |
| 2026-11-12 | Static research on the 24A446 kernelcache and monitors: symbolication with a third-party signature set, a KEXT import investigation, monitor structure counts, a memory-protection documentation re-read, and metadata comparison with the 24B119 and 24B156 builds. The v0.3.0 release was not created. Readiness is unchanged. | 부분 검증 | S-004, S-043, S-044, S-045, S-046 |

## 14. 검증된 주장

`verified` 판정에는 직접 확인되었거나 API로 확인된 1차 출처(또는 등급 1 출처)와 높은 신뢰도가 필요합니다. 각 주장의 적용 범위는 [data/claims.json](data/claims.json)에 있습니다.

| ID | 주장 | 신뢰도 | 출처 |
|---|---|---|---|
| C-002 | The reported demonstration device (iPhone 18 Pro) uses A20 Pro, so the demonstration is not direct evidence for A17 Pro | 높음 | S-005, S-010 |
| C-005 | Apple's iOS 27 security notes credit Calif.io researchers for four CVE entries (CVE-2026-65409, CVE-2026-65410, CVE-2026-28968 and CVE-2026-86886) | 높음 | S-001 |
| C-006 | Apple's iOS 27 security notes name Claude and Anthropic Research alongside Calif.io for two entries | 높음 | S-001 |
| C-007 | iOS 27.0.1 has no published CVE entries in Apple's security releases index | 높음 | S-002 |
| C-011 | Apple says Memory Integrity Enforcement is built into all iPhone 17 and iPhone Air models and names the A19 and A19 Pro chips | 높음 | S-003 |
| C-013 | Apple states SPTM is supported on A15-or-later and M2-or-later SoCs | 높음 | S-004 |
| C-016 | Dopamine 3.0 release notes state a Titan PPL/SPTM bypass for all devices on iOS 16.5.1 to 17.3.1 | 높음 | S-007, S-039 |
| C-017 | Dopamine 3.0.13 is the latest official Dopamine release (published 2026-11-03) | 높음 | S-007 |
| C-029 | A GitHub account with the login pwnlambda exists | 높음 | S-013 |
| C-032 | Apple states PPL and SPTM enforce execution of signed and trusted code on all platforms except macOS | 높음 | S-004 |
| C-033 | The five most recent Dopamine default-branch commit subjects do not mention iOS 27 | 높음 | S-032 |
| C-034 | Apple's iOS 27 notes list two kernel-component entries with arbitrary code execution with kernel privileges (CVE-2026-84607 and CVE-2026-86916) | 높음 | S-001 |
| C-035 | Apple's iOS 27 notes list eight kernel-memory read, disclosure, layout or state entries, one requiring root privileges | 높음 | S-001 |
| C-036 | Apple's iOS 27 notes list a kernel entry that lets a malicious app gain root privileges (CVE-2026-43689) | 높음 | S-001 |
| C-037 | Apple's iOS 27 notes list kernel-memory write and corruption entries, including the Calif.io-credited CVE-2026-28968 | 높음 | S-001 |
| C-038 | Apple's iOS 27 notes credit Calif.io for four entries with different components and impacts | 높음 | S-001 |
| C-039 | Apple's iOS 27.2 notes list 23 kernel-memory entries (4 write, 12 corruption, 1 copy-on-write, 6 read or disclosure) and no kernel or root privilege entry | 높음 | S-033 |
| C-040 | Apple's iOS 27.2 notes list six kernel-memory read, disclosure or layout entries from several components | 높음 | S-033 |
| C-041 | Apple's iOS 27.2 notes list further kernel-memory corruption and write entries in Apple Neural Engine and AVEVideoEncoder | 높음 | S-033 |
| C-042 | The six Calif.io-credited entries in Apple's iOS 27.2 notes carry no kernel read or write impact | 높음 | S-033 |
| C-043 | CVE-2026-112611 and CVE-2026-113912 credit a Calif.io-affiliated researcher by handle, but neither is a kernel entry | 높음 | S-033 |
| C-044 | Apple's entry for CVE-2026-112705 lists the AVEVideoEncoder component with an impact of unexpected system termination, not a kernel-level impact | 높음 | S-033 |
| C-045 | Apple's iOS 27.2.1 notes list nine CVE identifiers, none of them one of the six target kernel entries | 높음 | S-034 |
| C-047 | Apple's iOS 27.2 notes state no affected iOS versions for the listed entries | 높음 | S-033 |
| C-048 | Apple's iOS 27.2 notes list a WebContent sandbox-escape entry that a remote attacker may use (CVE-2026-112690) | 높음 | S-033 |
| C-055 | No Dopamine 3.0.x release note from 3.0.2 to 3.0.13 mentions iOS 27 support | 높음 | S-007 |
| C-056 | The repository formerly at evelyneee/ellekit redirects to tealbathingsuit/ellekit, which has no GitHub release | 높음 | S-040 |
| C-058 | A public GitHub repository named staturnzz/momentarius is described as an A12/A13 PPL bypass | 높음 | S-041 |
| C-059 | An independent SPTM analysis states that SPTM replaced PPL on A15 or newer and M2 or newer SoCs | 높음 | S-035, S-004 |
| C-060 | The arXiv SPTM analysis's firmware work uses an iPhone 16 on iOS 18.4. The paper does not analyse the A17 Pro or any iOS 27 build | 높음 | S-035 |
| C-065 | Dopamine 3.0 release notes state a Titan PPL/SPTM bypass for all devices on iOS 16.5.1 to 17.3.1 | 높음 | S-007 |
| C-066 | Dopamine 3.0 release notes say real-device SPTM support stops at iOS 17.3.1 because no SPTM bypass is known for iOS 17.4 and later | 높음 | S-007 |
| C-067 | Dopamine 3.0 release notes describe a momentarius PPL bypass for A12 and A13 devices on iOS 16.6 to 18.7.1 and 26.0 to 26.0.1 | 높음 | S-007, S-041 |
| C-068 | Dopamine 3.0 release notes name ClearSword and DarkSword workarounds but state no iOS version range for either exploit | 높음 | S-007 |
| C-070 | Apple's iOS 27 notes list CVE-2026-112608 (CoreMedia) as added on 2026-10-26 | 높음 | S-001 |
| C-071 | Apple's iOS 27 page marks 45 identifiers as added or updated on 2026-10-19 or 2026-10-26 | 높음 | S-001 |
| C-072 | Most Apple entries in iOS 27 and 27.2 apply to iPhone 11 and later; three Apple Intelligence entries apply to iPhone 15 Pro and later | 높음 | S-001, S-033 |
| C-073 | Apple's iOS 27 and iOS 27.2 notes do not mention AGX, IOGPU, SPTM, TXM, PPL, CoreTrust, AMFI or Exclave | 높음 | S-001, S-033 |
| C-074 | Apple's iOS 27 notes list four kernel or root privilege entries; the iOS 27.2 notes list none | 높음 | S-001, S-033 |
| C-078 | The 24A446 manifest's KernelCache digest equals the SHA-384 of the raw IM4P container (identities 0, 1 and 2) | 높음 | S-043 |
| C-079 | The analysed 24A446 kernelcache is the LZFSE decompression of the verified container (73,023,488 bytes, byte-identical) | 높음 | S-043 |
| C-080 | Restore-entry digests for the 24A446 kernelcache and the SPTM and TXM monitors do not match the retrieved containers | 높음 | S-043 |
| C-081 | The 24A446 package contains SPTM and TXM monitor containers that are unencrypted, with matching normal manifest digests | 높음 | S-043 |
| C-082 | The 24A446 kernelcache fileset contains the sandbox, AMFI, CoreTrust and Image4 bundles, by exact identifier | 높음 | S-043 |
| C-083 | The 24A446 kernelcache contains kernel log strings that name SPTM and TXM interfaces | 높음 | S-043 |
| C-086 | Standalone KEXT files extracted from the 24A446 kernelcache have empty symbol tables, and Ghidra cannot import them | 높음 | S-043 |
| C-088 | Ghidra's automatic analysis of the 24A446 TXM image completed without logged errors, recovering 1,654 functions (1,653 default-named) | 높음 | S-043 |
| C-089 | The 24B119 (27.2) manifest's KernelCache, SPTM and TXM normal digests match the retrieved containers | 높음 | S-044 |
| C-090 | The 24B119 (27.2) restore-entry digests for the kernelcache, SPTM and TXM do not match the retrieved containers | 높음 | S-044 |
| C-091 | The 24B156 (27.2.1) manifest's KernelCache, SPTM and TXM normal digests match the retrieved containers | 높음 | S-045 |
| C-092 | The 24B156 (27.2.1) restore-entry digests for the kernelcache, SPTM and TXM do not match the retrieved containers | 높음 | S-045 |
| C-093 | The SPTM and TXM containers of 24B119 and 24B156 are byte-identical to each other and differ from 24A446 | 높음 | S-043, S-044, S-045 |
| C-094 | The kernel version strings are darwin 27.0.0 (XNU 13432.2.10~2) for 24A446 and darwin 27.2.0 (XNU 13432.42.3~28) for 24B119 and 24B156 | 높음 | S-043, S-044, S-045 |
| C-095 | The KEXT inventories of 24B119 and 24B156 contain the same 281 records as 24A446; 47 bundle-version and 48 short-version fields differ from 24A446 in each | 높음 | S-043, S-044, S-045 |
| C-096 | The kernelcache and the SPTM and TXM monitor images of 24A446 carry the arm64e subtype bit in their Mach-O headers | 높음 | S-043 |
| C-097 | The signature set kernel/27.0 in the symbolicator repository declares a darwin range of 27.0.0 to 27.2.0 | 높음 | S-046 |
| C-098 | About 80% of the distinct xnu signature anchor strings occur in the 24A446 kernelcache | 높음 | S-043, S-046 |
| C-099 | Signature-assisted symbolication of the 24A446 kernel assigns non-equivalent names to 1,139 addresses | 높음 | S-043, S-046 |
| C-101 | Ghidra cannot import the standalone KEXT files extracted from the 24A446 kernelcache, because stub processing reads symbols from an empty table | 높음 | S-043 |
| C-102 | Of the 281 KEXT inventory records of 24A446, 263 match a fileset entry, 11 are codeless and 7 are kernel-programming-interface pseudo-KEXTs with no fileset entry | 높음 | S-043 |
| C-105 | Apple's Platform Security guide states that SPTM is supported on A15-or-later and M2-or-later SoCs, and that SPTM with TXM replaces the PPL there | 높음 | S-004 |
| C-106 | Apple's Platform Security guide states that Memory Integrity Enforcement is available on A19 and M5 processors or later | 높음 | S-004 |

## 15. 미검증 주장

부분 검증된 주장은 확인 가능한 근거가 있지만, 핵심 요소(범위, 빌드, 기기 또는 날짜)가 아직 검증되지 않았습니다. 미검증 주장은 단서로만 취급합니다.

### 부분 검증

| ID | 주장 | 신뢰도 | 출처 |
|---|---|---|---|
| C-001 | Calif.io reportedly demonstrated an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro at Hexacon 2026 | 중간 | S-005, S-010, S-011, S-012, S-036, S-037 |
| C-003 | iOS 27.0.1 build 24A446 is the build for iPhone16,2 (iPhone 15 Pro Max) | 중간 | S-014, S-015, S-016 |
| C-008 | iOS 27.2 (build 24B119) was released on 2026-10-26 | 중간 | S-002, S-014 |
| C-009 | iOS 27.2.1 (build 24B156) was released on 2026-11-09 | 중간 | S-002, S-014 |
| C-012 | A17 Pro is not among the chips Apple names for Memory Integrity Enforcement | 중간 | S-003 |
| C-014 | The A17 Pro falls within Apple's A15-or-later SPTM class | 중간 | S-004, S-030 |
| C-018 | No Dopamine release is documented to support iOS 27.0.1 on A17 Pro | 중간 | S-009, S-007, S-008 |
| C-019 | The usbliter8 BootROM exploit is reported to affect A12 and A13 chips and not A14 or later | 중간 | S-021, S-022, S-023 |
| C-024 | iOS 27.0.1 was released on 2026-09-28 | 중간 | S-002, S-014, S-016 |
| C-025 | The device identifier iPhone16,2 corresponds to the iPhone 15 Pro Max | 중간 | S-014 |
| C-026 | The iPhone 15 Pro Max uses the Apple A17 Pro chip | 중간 | S-030 |
| C-027 | No public complete exploit chain applicable to iPhone 15 Pro Max on iOS 27.0.1 has been verified | 중간 | S-010, S-019 |
| C-028 | No publicly installable jailbreak tool is verified for iOS 27.0.1 on A17 Pro | 중간 | S-010, S-019, S-009, S-007 |
| C-030 | The latest GitHub release of the repository named Sileo/Sileo is 2.5.1 (2024-10-08), and its notes do not mention iOS 27 | 중간 | S-031 |
| C-046 | Apple's iOS 27.2 notes contain 162 distinct CVE identifiers in the extracted text; press reports 163 | 중간 | S-033 |
| C-049 | No public kernel read/write write-up or exploit code by the researcher announced on 2026-11-04 was found as of 2026-11-12 | 중간 | S-013, S-029 |
| C-069 | 8kSec reports Apple's fixed-in versions for the two DarkSword kernel CVEs as iOS 26.2 and 26.3 (secondary analysis) | 중간 | S-042 |
| C-084 | The 24A446 kernelcache contains MIE-related strings; whether MIE is active on the A17 Pro is not established | 중간 | S-043 |
| C-085 | Ghidra recorded no code reference into the 24A446 __DATA_SPTM segment; the cause is unresolved | 중간 | S-043 |
| C-087 | Ghidra's automatic analysis of the 24A446 kernelcache completed, recovering 230,298 functions (3 named) with 17 logged errors | 중간 | S-043 |
| C-100 | On 58 kernel addresses that have independent table-derived names, signature names agree in 55 (94.8%) | 중간 | S-043, S-046 |
| C-103 | Ghidra's reference model records no register-indirect call references in the 24A446 SPTM or TXM images, while a byte-level decoder finds such encodings in both | 중간 | S-043 |
| C-104 | Four methods found no code path that addresses the 24A446 __DATA_SPTM segment; the cause of the absence is unresolved | 중간 | S-043 |
| C-107 | The A15-A18 column of the Platform Security guide's feature table includes the A17 generation; the support cells are not readable from the fetched copy | 중간 | S-004 |

### 미검증

| ID | 주장 | 신뢰도 | 출처 |
|---|---|---|---|
| C-004 | The demonstrated jailbreak state persisted across a reboot | 낮음 | S-010 |
| C-010 | iOS 27.2 fixed 163 vulnerabilities | 낮음 | S-017, S-018 |
| C-015 | A publicly disclosed SPTM bypass applies to A17 Pro on iOS 27.0.1 | 낮음 | S-026 |
| C-020 | A tutorial page claims a full iOS 27 jailbreak using usbliter8 | 낮음 | S-025 |
| C-021 | iOS 27.0.1 (24A446) is unsigned in the ipsw.me index on 2026-11-12, after a 2026-11-02 report that it was signed | 낮음 | S-014 |
| C-022 | A Calif.io-linked researcher reportedly announced a kernel read/write exploit and write-up within about a week | 낮음 | S-026, S-029 |
| C-023 | An Apple CVE credit confirms the identity of the lambda handle, according to the reference repository | 낮음 | S-026 |
| C-050 | opa334 is reported (2026-11-04) to plan A12/A13 Dopamine support via momentarius once a kernel read/write exploit is public, with A14 and later still needing an SPTM bypass | 낮음 | S-026 |
| C-051 | A 2026-10-17 opa334 statement is reported to warn of an SPTM bypass valid through iOS 27.0.1 (upstream V7) | 낮음 | S-026 |
| C-052 | A Calif.io researcher is reported to have said the jailbreak applies to any iPhone running iOS 27.0.1, possibly including iPads (upstream V10) | 낮음 | S-026 |
| C-053 | A Calif.io video is reported to show a jailbreak state surviving an over-the-air update to iOS 27.2 with Lockdown Mode enabled (upstream V32) | 낮음 | S-026 |
| C-054 | The upstream states that DarkSword and ClearSword kernel exploits support iOS only up to 26.0.1 (V8); no primary source confirms the range | 낮음 | S-026 |
| C-057 | ElleKit 1.2 is reported to cover iOS 15 to 27 (upstream reference) | 낮음 | S-026 |
| C-061 | Press coverage reports that AI helped build the Calif.io jailbreak (not confirmed by the team) | 낮음 | S-036, S-037, S-038 |
| C-062 | A third party is reported to have reproduced CVE-2026-112705 as a crash on iPhone 17 Pro, iOS 27.0.1 (unverified) | 낮음 | S-026 |
| C-063 | A company-branded account is reported to have shown a root shell on iOS 27.2 (unverified) | 낮음 | S-026 |
| C-064 | A project announced on 2026-11-01 claims a semi-untethered iOS 27.0 to 27.0.1 jailbreak for iPhone 15 Pro Max (A17 Pro); no release or validation was located | 낮음 | S-026 |
| C-075 | heise reports the Calif.io jailbreak as 'the first reboot-proof jailbreak since iOS 9' (press claim; unverified) | 낮음 | S-036 |
| C-076 | t3n reports AI-assisted exploit-chain discovery and an iOS 27.2 beta comparison as established; heise calls the comparison theoretical | 낮음 | S-038 |
| C-077 | The upstream reports a Calif.io team member saying the team will not release an end-user jailbreak tool (unverified) | 낮음 | S-026 |

## 16. 출처 색인

등급: 1 1차(Apple, 원저 연구, 공식 저장소 및 학회 사이트), 2 독립적 또는 신뢰할 만한 출처(언론, 정부 CERT, 제3자 색인, 백과사전), 3 커뮤니티, 4 확인 불가. 자세한 내용은 [docs/RESEARCH_METHODOLOGY.md](docs/RESEARCH_METHODOLOGY.md)를 참조하십시오.

| ID | 출처 | 발행처 | 등급 | 발행일 | 확인 방법 |
|---|---|---|---|---|---|
| S-001 | [About the security content of iOS 27 and iPadOS 27](https://support.apple.com/en-us/149034) | Apple Inc. | 1 | 2026-09-14 | 본문 확인 |
| S-002 | [Apple security releases](https://support.apple.com/en-us/100100) | Apple Inc. | 1 | - | 일부 본문 확인 |
| S-003 | [Memory Integrity Enforcement](https://security.apple.com/blog/memory-integrity-enforcement/) | Apple Inc. (Apple Security Research) | 1 | 2025-09 | 본문 확인 |
| S-004 | [Apple Platform Security: Secure Page Table Monitor and Trusted Execution Monitor](https://support.apple.com/guide/security/sec8b776536b/web) | Apple Inc. | 1 | - | 본문 확인 |
| S-005 | [iPhone 18 Pro - Technical Specifications](https://www.apple.com/iphone-18-pro/specs/) | Apple Inc. | 1 | - | 본문 확인 |
| S-006 | [iPhone 15 Pro - Technical Specifications](https://www.apple.com/iphone-15-pro/specs/) | Apple Inc. | 1 | - | 본문 확인 |
| S-007 | [Dopamine releases](https://github.com/opa334/Dopamine/releases) | opa334 (Dopamine project, GitHub) | 1 | 2026-11-03 | API 응답 |
| S-008 | [Dopamine repository README](https://github.com/opa334/Dopamine) | opa334 (Dopamine project, GitHub) | 1 | - | 본문 확인 |
| S-009 | [Dopamine 3.0 Jailbreak Released With iOS 17.3.1 Support, iOS 26 on A12/A13](https://www.iclarified.com/101697/dopamine-30-jailbreak-released-with-ios-1731-support-ios-26-on-a12a13) | iClarified | 2 | 2026-08-07 | 본문 확인 |
| S-010 | [Hackers Jailbreak iPhone 18 Pro on Stage, and It Survives a Reboot](https://decrypt.co/381177/hackers-jailbreak-iphone-18-pro-survives-reboot) | Decrypt | 2 | 2026-10-16 | 본문 확인 |
| S-011 | [Hexacon 2026](https://hexacon.fr) | Hexacon (conference organiser) | 1 | - | 본문 확인 |
| S-012 | [Calif.io](https://calif.io) | Calif.io | 1 | - | 본문 확인 |
| S-013 | [GitHub user record: pwnlambda](https://api.github.com/users/pwnlambda) | GitHub | 1 | - | API 응답 |
| S-014 | [ipsw.me device firmware index: iPhone16,2](https://api.ipsw.me/v4/device/iPhone16,2?type=ipsw) | ipsw.me | 2 | - | API 응답 |
| S-015 | [Keys:Rave 24A446 (iPhone16,2)](https://theapplewiki.com/wiki/Keys:Rave_24A446_(iPhone16,2)) | The Apple Wiki | 3 | - | 검색 결과 요약만 |
| S-016 | [iOS 27.0.1 bug fixes, changes and improvements](https://forums.macrumors.com/threads/ios-27-0-1-bug-fixes-changes-and-improvements.2490674/) | MacRumors Forums | 3 | - | 검색 결과 요약만 |
| S-017 | [Apple Fixes 163 iPhone, iPad Flaws in iOS 27.2 Update](https://www.esecurityplanet.com/threats/news-apple-ios-27-2-ipados-163-security-flaws/) | eSecurityPlanet | 2 | - | 검색 결과 요약만 |
| S-018 | [Apple Just Patched 163 iPhone Security Flaws - Here's What Was at Risk](https://www.techrepublic.com/article/news-ios-27-2-security-flaws-patched/) | TechRepublic | 2 | - | 검색 결과 요약만 |
| S-019 | [Calif's iPhone Jailbreak: Apple Patches Most Flaws in iOS 27.2, but No Public Tool Is Planned](https://pbxscience.com/califs-iphone-jailbreak-apple-patches-most-flaws-in-ios-27-2-but-no-public-tool-is-planned/) | PBX Science | 2 | - | 검색 결과 요약만 |
| S-020 | [No More Downgrading: Apple Stops Signing iOS 26.6.2 and iOS 26.7 Following Release of iOS 27](https://www.mactrast.com/2026/09/no-more-downgrading-apple-stops-signing-ios-26-6-2-and-ios-26-7-following-release-of-ios-27/) | MacTrast | 2 | - | 검색 결과 요약만 |
| S-021 | [Vulnerability in iPhones with A12 and A13 processors](https://www.incibe.es/en/incibe-cert/publications/cybersecurity-highlights/vulnerability-iphones-a12-and-a13-processors) | INCIBE-CERT (Spain) | 2 | - | 검색 결과 요약만 |
| S-022 | [Apple's A12 and A13 Chips Facing New Unpatchable Exploit](https://www.macrumors.com/2026/06/18/a12-and-a13-chips-facing-exploit/) | MacRumors | 2 | 2026-06-18 | 검색 결과 요약만 |
| S-023 | [usbliter8 Brings Unpatchable BootROM Exploit to Apple A12 and A13 Devices](https://securityaffairs.com/193965/hacking/usbliter8-brings-unpatchable-bootrom-exploit-to-apple-a12-and-a13-devices.html) | Security Affairs | 2 | - | 검색 결과 요약만 |
| S-024 | [Apple rains on MIE-bypassing iPhone jailbreak parade with iOS update](https://www.itnews.com.au/news/apple-rains-on-mie-bypassing-iphone-jailbreak-parade-with-ios-update-629978) | iTnews | 2 | 2026-11-03 | 검색 결과 요약만 |
| S-025 | [How usbliter8 enables a full jailbreak of iOS 27 (tutorial page)](https://www.besthub.dev/articles/how-usbliter8-enables-a-full-jailbreak-of-ios-27-complete-technical-guide-0a0ebb30bb7d) | Unknown (tutorial-style website) | 4 | - | 검색 결과 요약만 |
| S-026 | [iOS 27.0.1 Jailbreak Fact-Check and Ongoing Tracker (iMaxTomas/ios27-jb-tracker)](https://github.com/iMaxTomas/ios27-jb-tracker) | iMaxTomas (GitHub) | 3 | 2026-11-04 | 본문 확인 |
| S-027 | [Creative Commons Attribution 4.0 International - Legal Code](https://creativecommons.org/licenses/by/4.0/legalcode) | Creative Commons | 1 | - | 본문 확인 |
| S-028 | [Contributor Covenant Code of Conduct, version 2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) | Contributor Covenant project | 1 | - | 본문 확인 |
| S-029 | [PBX Science: Calif iPhone jailbreak coverage (2026-11-04)](https://pbxscience.com/?p=24999) | PBX Science | 2 | 2026-11-04 | 본문 확인 |
| S-030 | [iPhone 15 Pro](https://en.wikipedia.org/wiki/IPhone_15_Pro) | Wikipedia | 2 | - | 본문 확인 |
| S-031 | [Sileo/Sileo: latest GitHub release (2.5.1)](https://github.com/Sileo/Sileo/releases/tag/2.5.1) | Sileo project (GitHub repository named Sileo/Sileo) | 2 | 2024-10-08 | API 응답 |
| S-032 | [Dopamine default-branch commit history](https://github.com/opa334/Dopamine/commits) | opa334 (Dopamine project, GitHub) | 1 | 2026-11-03 | API 응답 |
| S-033 | [About the security content of iOS 27.2 and iPadOS 27.2](https://support.apple.com/en-us/149230) | Apple Inc. | 1 | 2026-10-26 | 본문 확인 |
| S-034 | [About the security content of iOS 27.2.1 and iPadOS 27.2.1](https://support.apple.com/en-us/149715) | Apple Inc. | 1 | 2026-11-09 | 본문 확인 |
| S-035 | [Modern iOS Security Features: A Deep Dive into SPTM, TXM, and Exclaves (arXiv:2510.09272)](https://arxiv.org/abs/2510.09272) | arXiv (independent academic analysis) | 2 | 2025-10-10 | 본문 확인 |
| S-036 | [Works on iPhone 18 Pro: AI helps create untethered jailbreak for iOS 27.0.1](https://www.heise.de/en/news/Works-on-iPhone-18-Pro-AI-helps-create-untethered-jailbreak-for-iOS-27-0-1-11490907.html) | heise online | 2 | 2026-10-16 | 본문 확인 |
| S-037 | [Dank KI: Rebootfester Jailbreak für iOS 27.0.1 bis zum iPhone 18 Pro, untethered](https://www.heise.de/news/Untethered-Jailbreak-fuer-iOS-27-0-1-auf-iPhone-18-Pro-der-Reboots-ueberlebt-11490726.html) | heise online | 2 | 2026-10-16 | 본문 확인 |
| S-038 | [iOS-27-Jailbreak: Sicherheitsforscher greifen auf KI-Support zurück](https://t3n.de/news/untethered-jailbreak-ios-27-1768775/) | t3n | 2 | 2026-10-18 | 본문 확인 |
| S-039 | [Dopamine Jailbreak (third-party page, ellekit.space)](https://ellekit.space/dopamine) | ellekit.space (authorship not verified) | 3 | - | 본문 확인 |
| S-040 | [tealbathingsuit/ellekit (repository reached by redirect from evelyneee/ellekit)](https://github.com/tealbathingsuit/ellekit) | GitHub (repository owner: tealbathingsuit) | 2 | - | API 응답 |
| S-041 | [staturnzz/momentarius (repository metadata)](https://api.github.com/repos/staturnzz/momentarius) | GitHub (repository owner: staturnzz) | 3 | 2026-08-07 | API 응답 |
| S-042 | [Inside the DarkSword Kernel Escalation: From GPU Process to Kernel R/W (CVE-2025-43510 & CVE-2025-43520)](https://www.8ksec.io/darksword-kernel-escalation-cve-2025-43510-43520/) | 8kSec | 2 | 2026-05-03 | 본문 확인 |
| S-043 | [iOS 27.0.1 (24A446) iPhone16,2 firmware package: BuildManifest and IM4P components (Apple CDN object)](https://updates.cdn-apple.com/2026FallFCS/531d0d56-6e43-4fb9-b4ee-abb5aab5c04f/iPhone16,2_27.0.1_24A446_Restore.ipsw) | Apple Inc. (CDN object listed by the ipsw.me firmware index) | 1 | 2026-09-28 | 일부 본문 확인 |
| S-044 | [iOS 27.2 (24B119) iPhone16,2 firmware package: BuildManifest and IM4P components (Apple CDN object)](https://updates.cdn-apple.com/2026FallFCS/dcf3b441-e473-4c28-a936-99d6af8c60a2/iPhone16,2_27.2_24B119_Restore.ipsw) | Apple Inc. (CDN object; URL resolved by a firmware index lookup) | 1 | 2026-10-26 | 일부 본문 확인 |
| S-045 | [iOS 27.2.1 (24B156) iPhone16,2 firmware package: BuildManifest and IM4P components (Apple CDN object)](https://updates.cdn-apple.com/2026FallFCS/079a8de1-4a8d-4aa2-b5fb-7c33a7ffbf19/iPhone16,2_27.2.1_24B156_Restore.ipsw) | Apple Inc. (CDN object; URL resolved by a firmware index lookup) | 1 | 2026-11-09 | 일부 본문 확인 |
| S-046 | [blacktop/symbolicator: ipsw symbolication signatures (kernel/27.0 folder, MIT licence)](https://github.com/blacktop/symbolicator) | blacktop/symbolicator repository (community; MIT licence) | 3 | 2026-11-05 | 일부 본문 확인 |

## 17. 기여 안내

새 출처, 정정, 근거가 있는 판정 변경, 사기 신고를 환영합니다. 먼저 [CONTRIBUTING.md](CONTRIBUTING.md)를 읽어 주십시오. 익스플로잇 코드, 도구 링크, 설치 패키지, 기기 식별자, 개인 정보는 절대 포함하지 마십시오. Pull request를 열기 전에 `python3 scripts/validate_tracker.py`를 실행하십시오.

관리자는 pull request의 코드를 실행하지 않으며, 외부 pull request는 자동으로 병합되지 않습니다.

## 18. 안전 정책

- 이 프로젝트는 iPhone에 연결하거나, 조작하거나, 그에 대한 작업을 권하지 않습니다. 탈옥을 연구할 권한이 있다고 해서 이를 실행할 권한이 있는 것은 아닙니다.
- 검증되지 않은 출처의 IPA 파일, 구성 프로파일, 탈옥 도구를 설치하지 마십시오. 증명되기 전까지 악성코드로 취급하십시오.
- 일련번호, UDID, ECID, IMEI, EID 값, Apple 계정 정보, 토큰, 백업, 기기 로그를 공개하거나 제출하지 마십시오.
- 이 프로젝트는 관리자가 소유한 기기에 연결하거나, 검사하거나, 수정하지 않습니다. 연구에 실제 기기 작업이 필요하지 않으며, 실제 기기에 대한 작업은 그 기기의 소유자가 해당 작업에 대해 명시적으로 허가해야 합니다.
- 전체 정책: [docs/SAFETY_POLICY.md](docs/SAFETY_POLICY.md). 보안 보고: [SECURITY.md](SECURITY.md).

## 19. 라이선스

- 원본 코드(스크립트, 스키마, 검증기, 워크플로): MIT. [LICENSE](LICENSE)를 참조하십시오.
- 원본 문서 및 연구 글: 관리자가 권리를 가진 범위에서 CC BY 4.0. [LICENSE-DOCS](LICENSE-DOCS)를 참조하십시오.

### 제3자 연구 출처 표기

- **커뮤니티 참고 자료:** [iMaxTomas/ios27-jb-tracker](https://github.com/iMaxTomas/ios27-jb-tracker)(S-026). 원본 내용은 그 저장소의 라이선스에 따라 CC BY 4.0입니다. 이 프로젝트는 방법론 검토와 단서 목록을 위해 README, SKILL.md, LICENSE를 읽었습니다. 텍스트는 복사하지 않았습니다. 그 결론은 독립적 확인 없이 채택하지 않았으며, 개인 이름에 관한 귀속은 여기에 옮기지 않았습니다.
- **언론 보도, 펌웨어 색인, 백과사전 문서**는 [data/sources.json](data/sources.json)에 개별적으로 인용되어 있습니다. 저작권은 각 권리자에게 있으며, 사실 확인과 논평을 위해 인용합니다.
- **Apple의 보안 공지 및 사양 페이지**는 사실 참고 자료로 인용합니다.

## 20. 면책 조항

- 이 프로젝트는 독립적인 연구 및 호환성 프로젝트입니다. Apple, Calif.io, Hexacon, Dopamine 프로젝트, Sileo의 승인, 후원 또는 보증을 받지 않았습니다.
- 탈옥 도구가 아니며, 탈옥 도구를 제공하지 않습니다.
- 정보는 연구 및 참고 목적으로만 제공됩니다. 법률, 보안 또는 기기 수리에 관한 조언이 아닙니다. 거주 지역의 법을 준수하고 기기 및 서비스 약관을 지키는 것은 소유자의 책임입니다.
- 데이터는 날짜가 기재된 스냅샷(2026-11-12)입니다. 상황은 빠르게 변하고 있습니다. 모든 기록의 `last_checked` 날짜를 확인하십시오.
