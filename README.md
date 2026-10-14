# DriveMate: Next-Gen Phone-as-a-Key & AI Automotive Copilot

> **Hackathon Edition**: Built with Flutter & Riverpod. Fully simulated vehicle telematics architecture ready to swap with ESP32 BLE or OEM Connected-Car APIs.

---

## Architecture Overview

```
Project-T/
├── lib/
│   ├── main.dart                       # Riverpod ProviderScope, GoRouter initialization
│   ├── theme/
│   │   ├── app_colors.dart             # Strict dark theme palette (#0C111B, #151C2B, etc.)
│   │   └── app_theme.dart              # Typography with Sora (weights 500 & 700), 18px radii
│   ├── models/
│   │   ├── vehicle_state.dart          # Telematics state (locked, engine, coolant, tyres, etc.)
│   │   ├── digital_key.dart            # BLE token model with live expiry countdown
│   │   ├── chat_message.dart           # Copilot conversational & action dispatch model
│   │   └── health_prediction.dart      # Algorithmic threshold & hours-to-failure predictor
│   ├── services/
│   │   ├── vehicle_service.dart        # Clean VehicleService interface + SimulatedVehicleService (2s ticker)
│   │   ├── ai_assistant_service.dart   # Gemini API integration with offline rule-based fallback
│   │   ├── voice_service.dart          # FlutterTTS & SpeechToText with safe hardware fallbacks
│   │   └── biometric_service.dart      # LocalAuth biometric gating with emulator pass-through
│   ├── providers/
│   │   ├── vehicle_provider.dart       # StateNotifier for telematics and live prediction stream
│   │   ├── assistant_provider.dart     # Conversational state and speech dispatcher
│   │   └── security_provider.dart      # Key lifecycle manager with 1s countdown ticker
│   ├── screens/
│   │   ├── main_scaffold.dart          # 4-tab bottom navigation (Drive, Assistant, Health, Security)
│   │   ├── drive_screen.dart           # Side-view vector, 112px Hold-to-Start, Lock/Unlock, Stats
│   │   ├── assistant_screen.dart       # Chat bubbles, quick chips, mic input, spoken answers
│   │   ├── health_screen.dart          # 270° Ring gauge, prediction tiles, Find Mechanic CTA
│   │   └── security_screen.dart        # Key tokens, auto-lock switches, simple vector map
│   └── widgets/
│       ├── car_vector.dart             # CustomPainter side-view coupe vector with headlights
│       ├── hold_to_start_button.dart   # 112px circular button with 1-second radial progress
│       ├── gauge_painter.dart          # Arc gauge with animated health score
│       ├── prediction_tile.dart        # Diagnostic item with severity dot and cause
│       ├── simple_map_widget.dart      # Dark vector GPS map with pulsing vehicle pin
│       ├── mechanic_sheet.dart         # Certified nearby mechanics with Call & WhatsApp
│       ├── trip_log_sheet.dart         # Trip history and energy efficiency log
│       └── crash_alert_dialog.dart     # Crash sensor impact test with 10s auto-SOS
├── test/
│   ├── health_prediction_test.dart     # Threshold calculation unit tests
│   └── vehicle_service_test.dart       # Telematics state transition unit tests
├── web_preview/
│   └── index.html                      # Standalone 1:1 interactive demo runner for Chrome
├── serve_demo.py                       # One-click demo server script
└── pubspec.yaml                        # Flutter package configuration
```

---

## How to Run

### Option A: Interactive Browser Runner (Zero-Setup, Tested on Google Chrome)
Since Flutter/Android SDK may require high-bandwidth downloads on new machines, a **1:1 pixel-perfect interactive web runner** is included:
```bash
# In PowerShell / Command Prompt:
python serve_demo.py
# Or directly open in Chrome:
start "C:\Program Files\Google\Chrome\Application\chrome.exe" "c:\Users\thanush\Desktop\Project-T\web_preview\index.html"
```

### Option B: Flutter Mobile App (Android / iOS / Web)
Once Flutter SDK is in your PATH:
```bash
# 1. Install dependencies
flutter pub get

# 2. Set optional Gemini API key (optional: offline fallback is built-in)
# export GEMINI_API_KEY="your-api-key"

# 3. Run on connected Android device or emulator
flutter run
```

---

## 3-Minute Demo Script for Judges

| Timestamp | Screen | Action | Voice / Visual Feedback |
|:---|:---|:---|:---|
| **0:00 - 0:30** | **Drive** | Tap **Unlock** (filled button), then **Lock** (outlined). Notice real-time status transitions. | Status toggles between "Parked, locked" and "Parked, unlocked". BLE key indicator is steady green. |
| **0:30 - 0:55** | **Drive** | **Press and hold the circular 112px button for 1 second**. | Circular progress ring fills over 1s, triggers biometric check, headlights illuminate on car vector, button animates to **Engine on**. Audio announces "Engine started". |
| **0:55 - 1:25** | **Assistant** | Switch to **Assistant** tab. Tap suggestion chip **"Tyre pressure"** or click mic. | Copilot answers: *"Rear-Left tyre is low at 28.5 PSI..."* in spoken audio. Ask *"Lock the car"* -> doors lock automatically. |
| **1:25 - 2:05** | **Drive & Health** | On Drive screen, **long-press the amber "Demo mode" tag** for 1.5s to inject a fault! | Status becomes **Fault active**. Voice warning announces: *"Warning: Coolant temperature rapidly escalating..."* Switch to **Health** tab: score drops from **78 (green)** to **42 (red)**. Prediction row displays *"Coolant rising: Service in ~6 hours"*. |
| **2:05 - 2:30** | **Health** | Tap **"Find a mechanic"**. | Bottom sheet slides up with certified mechanics, distance ratings, and direct **Call Shop** and **WhatsApp** buttons. |
| **2:30 - 3:00** | **Security** | Switch to **Security** tab. Tap **"Share a temporary key"** -> Authenticate biometrics -> Issue key. Observe live second-by-second countdown. Tap **Revoke** on Sophia's key -> token revoked instantly. Toggle **"Find my car"** to inspect parked vector map. |

---

## Clearly Labeled Sample Data & Estimates
All vehicle telematics in this demo are generated by `SimulatedVehicleService`:
* **Coolant Temperature**: Simulated nominal baseline 88.5°C - 91.5°C; escalated to 108.5°C on fault injection.
* **Tyre Pressures**: FL: 33 PSI, FR: 33 PSI, RL: 28.5 PSI (low trigger), RR: 33 PSI.
* **Time-to-Service Prediction**: Evaluated using threshold rules ($\Delta T / \Delta t$ temperature regression) predicting a ~6-hour threshold limit.
* **GPS Location**: Bay St / Financial District coordinates (`37.7749, -122.4194`) with synthetic vector map grid.
* **Biometric Auth**: Integrated with `local_auth`; gracefully falls back to mock confirmation on emulators without fingerprint enrollments.

---

## Scope Adjustments & Cuts (Honest Engineering Log)
* **What We Kept (100% Implemented)**:
  - Phone-as-key workflow with 112px 1s hold-to-start.
  - Full dark mode palette & Sora typography with 0 emojis.
  - Riverpod state management & offline-first AI assistant fallback.
  - Predictive health ring gauge & threshold failure modeling.
  - Digital key sharing with live countdown and immediate revoke.
  - Biometric lock gating.
  - Nice-to-haves: Nearby mechanic sheet with Call/WhatsApp, trip log sheet, and crash detection auto-SOS dialog.
* **What We Cut to Protect Deadline**:
  - Direct OBD-II CAN bus connection (explicitly disallowed by scope rule).
  - Heavy Google Maps SDK native binary (replaced with lightweight zero-API-key dark vector canvas to prevent black-screen crashes on emulators).
