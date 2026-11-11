# iOS 27 A17 Pro 탈옥 추적기

**iPhone 15 Pro Max**(Apple A17 Pro, 기기 식별자 `iPhone16,2`)의 **iOS 27.0.1**(빌드 `24A446`)에 관한 독립 연구 및 호환성 추적 저장소입니다.

> **현재 상태(2026-11-11 기준 데이터): NO-GO. 대상 기기 준비도 LEVEL 0.** 이 기기와 빌드에 대해 검증된 탈옥은 아직 없습니다. 이 저장소는 탈옥 도구가 아니며, 익스플로잇 코드, 도구, 설치 절차를 제공하지 않습니다.

## 1. 프로젝트 소개

이 저장소는 iOS 27.0.1(빌드 24A446)의 iPhone 15 Pro Max 탈옥 연구에 관한 공개 정보를 수집하고, 검증하고, 점수화합니다. 독립적인 연구 및 호환성 프로젝트이며, Apple, Calif.io, Hexacon, Dopamine 프로젝트와 제휴 관계가 없습니다.

모든 주장은 출처, 날짜, 적용 범위, 판정, 한계와 함께 기록합니다. 언론 보도에만 근거한 내용은 "보도됨(reported)"으로 표시합니다. 커뮤니티 주장은 1차 출처가 확인하기 전까지 단서로만 취급합니다.

**AI 보조 사용 공개.** 초안 작성과 연구 보조는 Anthropic이 만든 AI 모델 Claude가 수행했습니다. 관리자가 결과를 검토하며, 모든 주장에는 출처가 있습니다. Apple의 iOS 27 보안 공지는 두 개의 CVE 항목에서 Calif.io와 함께 "Claude and Anthropic Research"를 명시합니다(C-006). 이 프로젝트는 Apple의 표현을 그대로 인용할 뿐, 그 협업 방식에 대해 추론하지 않습니다. 이 프로젝트는 관리자가 독립적으로 운영하며, Anthropic의 제품이 아닙니다.

## 2. 프로젝트 목표

- 대상 기기와 빌드에 대해 탈옥 경로가 존재하는지 근거로 확정합니다.
- 탈옥으로 이어질 수 있는 연구 영역을 추적합니다: SPTM, 커널 연구, 샌드박스 탈출과 권한 상승, 빌드 호환성, 익스플로잇 체인 통합, 탈옥 생태계, 지속성, 사기 탐지.
- 사용자의 주력 기기를 보호합니다. 이 프로젝트는 해당 기기에 연결하지 않으며, 기기에 대한 작업을 권하지 않습니다.
- 펌웨어 사실관계를 정확하게 유지합니다: 설치된 빌드, 서명 상태, 알려지지 않은 사항.
- 다른 사람들이 확인, 정정, 재사용할 수 있도록 근거를 공개합니다(19절의 라이선스).

## 3. 대상 하드웨어

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
| 서명 상태 | 미해결. 제3자 색인은 이 빌드를 서명되지 않음으로 표시합니다. 커뮤니티 참고 자료는 2026-11-02에 서명됨으로 보고했습니다(C-021). |
| 소유자 보고 기준선 | 설치된 빌드 iOS 27.0.1(24A446). 소유자는 이 빌드가 서명되지 않았다고 보고했으며(제3자 색인과 일치), 무선 업데이트(OTA) 차단이 켜져 있다고 보고했습니다. 이 프로젝트는 두 가지 모두 검증하지 않았습니다. |

대상은 고정되어 있습니다. 소유자는 연구 기기에 iOS 27.0.1(빌드 24A446)이 설치되어 있다고 보고했습니다. 이 프로젝트는 기기에 연결하거나 조회하지 않으므로 이를 검증할 수 없습니다.

## 5. 연구 현황

**데이터 스냅샷(2026-11-11):** 주장 32건(검증됨 10, 부분 검증 15, 미검증 7), 출처 32건, 타임라인 사건 17건, 호환성 행 15건, 펌웨어 빌드 4건.

**현재 위치: 대상 기기 LEVEL 0.** Calif.io가 2026-10-16에 iPhone 18 Pro(A20 Pro)에서 iOS 27.0.1 untethered 탈옥을 시연했다고 보도되었습니다(C-001, 부분 검증). 그 시연은 대상 기기를 사용하지 않았습니다. 검증된 기술 문서나 도구는 없습니다. Dopamine의 문서화된 A15~A17 지원 범위는 iOS 17.3.1에서 끝나며, A17 Pro에 대한 iOS 27 지원은 문서화되어 있지 않습니다(C-018).

영역별 연구 현황(세부 내용은 [research/](research/)):

| 영역 | 상태 |
|---|---|
| DIM01 사건 검증 | 부분 연구 |
| DIM02 A17 Pro 아키텍처 | 부분 연구 |
| DIM03 SPTM 연구 | 부분 연구 |
| DIM04 커널 취약점 정보 | 부분 연구 |
| DIM05 샌드박스 탈출 및 권한 상승 | 심층 연구 미완료 |
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
| CMP-003 | Kernel Vulnerability | 미검증 | C-005 | Apple credits Calif.io for iOS 27 entries, including a kernel-memory impact on CVE-2026-28968. |
| CMP-004 | Kernel Read | 미검증 | C-022 | A kernel read primitive is reported as planned by a Calif.io-linked researcher. |
| CMP-005 | Kernel Write | 미검증 | C-022 | Same basis as CMP-004. |
| CMP-006 | Sandbox Escape | 확정되지 않음 | - | No verified public sandbox escape for this target. |
| CMP-007 | Privilege Escalation | 확정되지 않음 | - | No verified public privilege escalation for this target. |
| CMP-008 | AMFI Compatibility | 미연구 | - | AMFI (code signing enforcement) was not researched in this pass. |
| CMP-009 | Complete Exploit Chain | 보도됨, 미검증 | C-001, C-002, C-027 | A complete chain is reported only for an iPhone 18 Pro (A20 Pro) demonstration. |
| CMP-010 | Bootstrap | 확정되지 않음 | C-016 | No bootstrap for iOS 27.0.1 is verified. |
| CMP-011 | Package Manager | 확정되지 않음 | C-030 | Sileo: the repository named Sileo/Sileo has 2.5.1 (2024-10-08) as its latest release, and its notes do not mention iOS 27. |
| CMP-012 | Persistence | 보도됨, 미검증 | C-004 | Reboot persistence is reported for an iPhone 18 Pro demonstration, not for the target. |
| CMP-013 | Public Jailbreak Tool | 확정되지 않음 | C-028 | No publicly installable tool is verified for this target. |
| CMP-014 | Independent A17 Pro Reproduction | 확정되지 않음 | - | No independent reproduction on A17 Pro hardware was found. |
| CMP-015 | Exact Build Verification | 부분 검증 | C-003, C-024, C-025 | Build 24A446 for iPhone16,2 is corroborated by third-party sources and by the Apple index date. |

모든 행은 대상 프로필(iPhone16,2, A17 Pro, iOS 27.0.1, 빌드 24A446)에 맞춰 적용됩니다. `not_established`는 해당 행에 검증된 근거가 없다는 뜻이며, 답이 "아니오"라는 뜻이 아닙니다.

## 7. SPTM 연구

- Apple은 SPTM이 A15 이상 및 M2 이상 SoC에서 지원되며, 지원되는 플랫폼에서 PPL을 대체한다고 밝혔습니다(C-013). 순서상 A17 Pro가 여기에 포함됩니다(C-014, 부분 검증).
- 대상 A17 Pro에 대한 공개 SPTM 우회는 검증되지 않았습니다. 커뮤니티 참고 자료는 공개되지 않은 우회를 보고하지만, 이는 미검증입니다(C-015).
- Dopamine의 문서화된 A15~A17 범위는 iOS 17.3.1에서 끝나며(C-016), iOS 27.0.1은 포함하지 않습니다.

세부 내용: [research/DIM03-sptm-research.md](research/DIM03-sptm-research.md).

## 8. 커널 연구

- Apple의 iOS 27 보안 공지는 Calif.io 연구자를 CVE-2026-65409, CVE-2026-65410, CVE-2026-28968, CVE-2026-86886 네 개 항목에 대해 인정합니다(C-005). 한 항목의 영향 문구는 "커널 메모리 손상"이고, 다른 항목의 영향 문구는 "보호된 시스템 파일 수정"입니다. iOS 27.0.1 또는 A17 Pro에 대한 적용 여부는 확정되지 않았습니다.
- Apple 색인은 27.0.1에 공개된 CVE 항목이 없다고 나열합니다(C-007).
- 커널 읽기/쓰기 공개가 예정되었다고 보도되었으나, 1차 출처 릴리스는 찾지 못했습니다(C-022, 미검증).
- 대상에 대해 검증된 공개 커널 익스플로잇은 없습니다.

세부 내용: [research/DIM04-kernel-vulnerability.md](research/DIM04-kernel-vulnerability.md).

## 9. 익스플로잇 체인 현황

- 보고된 유일한 완전한 체인은 iPhone 18 Pro(A20 Pro)에서 시연되었습니다. 기술 문서는 공개되지 않았고 구성 요소도 공개되지 않았습니다(C-001, C-027).
- 대상 기기에 대해 검증된 완전한 체인은 없습니다. 준비도: LEVEL 0.
- 이 프로젝트는 익스플로잇 코드를 공개하거나, 실행하거나, 설명하지 않습니다.

세부 내용: [research/DIM07-exploit-chain.md](research/DIM07-exploit-chain.md).

## 10. 탈옥 생태계

- **Dopamine:** 최신 공식 릴리스는 3.0.13(2026-11-03, C-017)입니다. 최근 커밋 제목 5개는 iOS 27을 언급하지 않습니다(C-033). 문서화된 지원 범위는 A15~A17에 대해 iOS 17.3.1에서 끝나며(C-016), A17 Pro에 대한 iOS 27 지원은 문서화되어 있지 않습니다(C-018).
- **Sileo:** Sileo/Sileo 저장소의 최신 릴리스는 2.5.1(2024-10-08)입니다. 릴리스 노트는 iOS 27을 언급하지 않습니다(C-030, 부분 검증).
- **ElleKit:** 이번 점검에서 공식 상류 저장소를 확인하지 못했습니다. 상태는 확정되지 않았습니다.
- **BootROM 문제:** A12 및 A13 칩에 대해 보고되었으며, A17 Pro는 해당하지 않는 것으로 보고되었습니다(C-019, 부분 검증).

세부 내용: [research/DIM08-jailbreak-ecosystem.md](research/DIM08-jailbreak-ecosystem.md).

## 11. 일상 사용 준비도

**평가되지 않음.** 대상에 대해 검증된 탈옥이 없으므로, 안정성, 배터리, Face ID, 뱅킹 및 인증 앱, 그 밖의 일상 사용 항목을 평가할 근거가 없습니다. LEVEL 6에 도달하지 않았습니다. 세부 내용: [research/DIM11-daily-driver-stability.md](research/DIM11-daily-driver-stability.md).

## 12. 펌웨어 보존

| 버전 | 빌드 | 출시일 | 서명 상태(기록) | Apple CVE 상태 |
|---|---|---|---|---|
| 27.0 | 24A437 | 2026-09-14 | 서명 안 됨(제3자 색인), 2026-11-12 | Apple 페이지에 나열됨 |
| 27.0.1 | 24A446 | 2026-09-28 | 서명 안 됨(제3자 색인), 2026-11-12 | 공개 없음 |
| 27.2 | 24B119 | 2026-10-26 | 서명됨(제3자 색인), 2026-11-12 | 찾지 못함 |
| 27.2.1 | 24B156 | 2026-11-09 | 서명됨(제3자 색인), 2026-11-12 | 찾지 못함 |

- 설치된 빌드는 복원 가능한 빌드와 같지 않습니다. 복원은 복원 시점의 Apple 서명에 달려 있습니다.
- 24A446의 서명 상태는 미해결입니다(C-021). 이 빌드로의 복원이 가능하다고 가정하지 마십시오.
- SHSH blob은 복원을 보장하지 않습니다.
- 이 프로젝트는 업데이트나 다운그레이드를 권하지 않습니다. 그 결정은 기기 소유자의 몫입니다.
- 소유자 보고: 무선 업데이트(OTA) 차단이 켜져 있습니다. 차단 방식과 적용 범위는 검증되지 않았으며, 모든 업데이트 또는 복원 경로를 막는다고 보장하지 않습니다.
- 실험 실패나 복구 시도로 더 새로운 펌웨어가 설치될 수 있으며, 그러면 iOS 27.0.1 연구 기준선이 끝납니다. 이 프로젝트는 그런 위험을 수반하는 작업을 권하지 않습니다.

세부 내용: [docs/RECOVERY_AND_PRESERVATION.md](docs/RECOVERY_AND_PRESERVATION.md)와 [reports/firmware-report.md](reports/firmware-report.md).

## 13. 연구 타임라인

| 날짜 | 사건 | 검증 상태 | 출처 |
|---|---|---|---|
| 2025-09 | Apple announces Memory Integrity Enforcement with the iPhone 17 and iPhone Air, naming the A19 and A19 Pro chips. | 검증됨 | S-003 |
| 2026-06-18 | usbliter8 BootROM exploit for A12 and A13 devices is publicised (reported by secondary outlets and a national CERT). | 부분 검증 | S-021, S-022, S-023 |
| 2026-08-07 | Dopamine 3.0 released; secondary coverage quotes a support table of iOS 15.0 to 17.3.1 for A8 to A17 and M1 to M2, and iOS 26.0 to 26.0.1 for A12 and A13. | 부분 검증 | S-009 |
| 2026-09-14 | iOS 27.0 released (build 24A437 per the third-party index). | 부분 검증 | S-014, S-001 |
| 2026-09-21 | Press reports Apple stopped signing iOS 26.6.2 after iOS 27 shipped. Used as a pattern example for how older builds lose signing. | 부분 검증 | S-020 |
| 2026-09-28 | iOS 27.0.1 released (build 24A446). Apple's security releases index lists no published CVE entries for this build. | 부분 검증 | S-002, S-014, S-016 |
| 2026-10-16 | Calif.io reportedly demonstrates an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro at Hexacon 2026 in Paris. | 부분 검증 | S-010, S-011, S-012 |
| 2026-10-19 | Apple's iOS 27 security notes are updated with CVE entries credited to Calif.io researchers, two of them jointly with Claude and Anthropic Research. | 검증됨 | S-001 |
| 2026-10-23 | Apple's index lists iOS 27.1 for iPhone Duo with no published CVE entries. | 검증됨 | S-002 |
| 2026-10-26 | iOS 27.2 released (build 24B119 per the third-party index). Secondary press reports 163 fixed vulnerabilities; Apple's 27.2 advisory was not located. | 부분 검증 | S-002, S-014, S-017, S-018 |
| 2026-11-02 | A community reference states that iOS 27.0.1 was still signed on 2026-11-02. This is not independently verified and conflicts with the third-party index checked on 2026-11-11. | 미검증 | S-026 |
| 2026-11-03 | Dopamine 3.0.13 published. Release notes describe a posix_spawn hook fix and a SpringBoard snapshot change. They do not state iOS 27 support. | 검증됨 | S-007 |
| 2026-11-03 | Press reports that Apple responded to MIE-bypass claims with an iOS update. Details were not verified. | 미검증 | S-024 |
| 2026-11-04 | Reported plan for a kernel read/write exploit and write-up from a Calif.io-linked researcher within about a week. Coverage conflicts; no primary announcement was located. | 미검증 | S-026, S-029 |
| 2026-11-06 | Press coverage through about 2026-11-06 reports that Apple fixed most flaws in iOS 27.2 and that no public tool is planned. | 부분 검증 | S-019 |
| 2026-11-09 | iOS 27.2.1 released (build 24B156 per the third-party index and the Wikipedia infobox). | 부분 검증 | S-002, S-014, S-030 |
| 2026-11-11 | Tracker snapshot. The third-party index lists iOS 27.0.1 as not signed. A community reference reports the opposite for 2026-11-02, so the status is unresolved. | 부분 검증 | S-014, S-026 |

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
| C-017 | Dopamine 3.0.13 is the latest official Dopamine release (published 2026-11-03) | 높음 | S-007 |
| C-029 | A GitHub account with the login pwnlambda exists | 높음 | S-013 |
| C-032 | Apple states PPL and SPTM enforce execution of signed and trusted code on all platforms except macOS | 높음 | S-004 |
| C-033 | The five most recent Dopamine default-branch commit subjects do not mention iOS 27 | 높음 | S-032 |

## 15. 미검증 주장

부분 검증된 주장은 확인 가능한 근거가 있지만, 핵심 요소(범위, 빌드, 기기 또는 날짜)가 아직 검증되지 않았습니다. 미검증 주장은 단서로만 취급합니다.

### 부분 검증

| ID | 주장 | 신뢰도 | 출처 |
|---|---|---|---|
| C-001 | Calif.io reportedly demonstrated an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro at Hexacon 2026 | 중간 | S-010, S-011, S-012, S-005 |
| C-003 | iOS 27.0.1 build 24A446 is the build for iPhone16,2 (iPhone 15 Pro Max) | 중간 | S-014, S-015, S-016 |
| C-008 | iOS 27.2 (build 24B119) was released on 2026-10-26 | 중간 | S-002, S-014 |
| C-009 | iOS 27.2.1 (build 24B156) was released on 2026-11-09 | 중간 | S-002, S-014 |
| C-012 | A17 Pro is not among the chips Apple names for Memory Integrity Enforcement | 중간 | S-003 |
| C-014 | The A17 Pro falls within Apple's A15-or-later SPTM class | 중간 | S-004, S-030 |
| C-016 | Dopamine 3.0 lists iOS 16.5.1 to 17.3.1 support for A15, A16, A17 and M2 devices | 중간 | S-009, S-007 |
| C-018 | No Dopamine release is documented to support iOS 27.0.1 on A17 Pro | 중간 | S-009, S-007, S-008 |
| C-019 | The usbliter8 BootROM exploit is reported to affect A12 and A13 chips and not A14 or later | 중간 | S-021, S-022, S-023 |
| C-024 | iOS 27.0.1 was released on 2026-09-28 | 중간 | S-002, S-014, S-016 |
| C-025 | The device identifier iPhone16,2 corresponds to the iPhone 15 Pro Max | 중간 | S-014 |
| C-026 | The iPhone 15 Pro Max uses the Apple A17 Pro chip | 중간 | S-030 |
| C-027 | No public complete exploit chain applicable to iPhone 15 Pro Max on iOS 27.0.1 has been verified | 중간 | S-010, S-019 |
| C-028 | No publicly installable jailbreak tool is verified for iOS 27.0.1 on A17 Pro | 중간 | S-010, S-019, S-009, S-007 |
| C-030 | The latest GitHub release of the repository named Sileo/Sileo is 2.5.1 (2024-10-08), and its notes do not mention iOS 27 | 중간 | S-031 |

### 미검증

| ID | 주장 | 신뢰도 | 출처 |
|---|---|---|---|
| C-004 | The demonstrated jailbreak state persisted across a reboot | 낮음 | S-010 |
| C-010 | iOS 27.2 fixed 163 vulnerabilities | 낮음 | S-017, S-018 |
| C-015 | A publicly disclosed SPTM bypass applies to A17 Pro on iOS 27.0.1 | 낮음 | S-026 |
| C-020 | A tutorial page claims a full iOS 27 jailbreak using usbliter8 | 낮음 | S-025 |
| C-021 | iOS 27.0.1 (24A446) is currently unsigned by Apple | 낮음 | S-014 |
| C-022 | A Calif.io-linked researcher reportedly announced a kernel read/write exploit and write-up within about a week | 낮음 | S-026, S-029 |
| C-023 | An Apple CVE credit confirms the identity of the lambda handle, according to the reference repository | 낮음 | S-026 |

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
| S-029 | [PBX Science: Calif iPhone jailbreak coverage (2026-11-04)](https://pbxscience.com/?p=24999) | PBX Science | 2 | 2026-11-04 | 검색 결과 요약만 |
| S-030 | [iPhone 15 Pro](https://en.wikipedia.org/wiki/IPhone_15_Pro) | Wikipedia | 2 | - | 본문 확인 |
| S-031 | [Sileo/Sileo: latest GitHub release (2.5.1)](https://github.com/Sileo/Sileo/releases/tag/2.5.1) | Sileo project (GitHub repository named Sileo/Sileo) | 2 | 2024-10-08 | API 응답 |
| S-032 | [Dopamine default-branch commit history](https://github.com/opa334/Dopamine/commits) | opa334 (Dopamine project, GitHub) | 1 | 2026-11-03 | API 응답 |

## 17. 기여 안내

새 출처, 정정, 근거가 있는 판정 변경, 사기 신고를 환영합니다. 먼저 [CONTRIBUTING.md](CONTRIBUTING.md)를 읽어 주십시오. 익스플로잇 코드, 도구 링크, 설치 패키지, 기기 식별자, 개인 정보는 절대 포함하지 마십시오. Pull request를 열기 전에 `python3 scripts/validate_tracker.py`를 실행하십시오.

관리자는 pull request의 코드를 실행하지 않으며, 외부 pull request는 자동으로 병합되지 않습니다.

## 18. 안전 정책

- 이 프로젝트는 iPhone에 연결하거나, 조작하거나, 그에 대한 작업을 권하지 않습니다. 탈옥을 연구할 권한이 있다고 해서 이를 실행할 권한이 있는 것은 아닙니다.
- 검증되지 않은 출처의 IPA 파일, 구성 프로파일, 탈옥 도구를 설치하지 마십시오. 증명되기 전까지 악성코드로 취급하십시오.
- 일련번호, UDID, ECID, IMEI, EID 값, Apple 계정 정보, 토큰, 백업, 기기 로그를 공개하거나 제출하지 마십시오.
- 소유자의 주력 기기는 현 상태 그대로 보존됩니다. 펌웨어, OTA 차단, 구성을 바꾸지 않고, DFU나 복구 모드를 쓰지 않으며, 연구를 위해 재부팅하지 않습니다.
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
- 데이터는 날짜가 기재된 스냅샷(2026-11-11)입니다. 상황은 빠르게 변하고 있습니다. 모든 기록의 `last_checked` 날짜를 확인하십시오.
