flowchart TD
A[Order Initiation]
A --> B[Buyer posts RFP]
A --> C[Seller lists material]
B & C --> D[Start Negotiation]
D --> E["System: 'This is an [Offer/Request] created by [User Name]'"]
E --> F[Action Buttons]

%% ===== Negotiation Action Buttons =====
F --> G[Propose New Price]
F --> H[Change Quantity]
F --> I[Change Pickup/Delivery Terms]
F --> J[Quality, Weather, Hold Options]
F --> K[Accept Offer]
F --> L[Cancel Offer]

%% ===== PRICE NEGOTIATION =====
G --> G1["Choose Price Option"]
G1 --> G2["Can you offer a discount / reduce price by ₹[X]?"]
G1 --> G3["Final Price — Not Negotiable"]
G1 --> G4["Offering [X]% off for quick confirmation"]
G1 --> G5["My budget is ₹[Input] — can you match?"]

G2 --> L1{Seller Response}
L1 -->|Accept Offer| M[Confirm Order]
L1 -->|Cancel Negotiation| N[End Negotiation]
L1 -->|Counter Offer ₹Z| O[Buyer Receives Counter Offer ₹Z]

O --> P{Buyer Response}
P -->|Accept Offer| M
P -->|Cancel Negotiation| N
P -->|Counter Offer ₹Y| Q[Seller Receives Counter Offer ₹Y]

Q --> R{Seller Response}
R -->|Accept Offer| M
R -->|Cancel Negotiation| N
R -->|Counter Offer ₹W| S[Buyer Receives Counter Offer ₹W]

S --> T{Buyer Response}
T -->|Accept Offer| M
T -->|Cancel Negotiation| N
T -->|Counter Offer ₹V| U["Seller Receives Counter Offer ₹V (Final Round)"]

U --> V{Final Seller Response}
V -->|Accept Offer| M
V -->|Cancel Negotiation| N
V -->|"⚠️ No further counters"| W[Accept/Cancel Only]

G3 --> X{Buyer Response}
X -->|Accept| M
X -->|Cancel| N

G4 --> Y{Buyer Response}
Y -->|Accept| M
Y -->|Cancel| N

G5 --> Z{Seller Response}
Z -->|"Matched" Offer| AA{Buyer Response}
Z -->|"Closest offer: ₹[Value]"| AA
AA -->|Accept| M
AA -->|Cancel| N

%% ===== QUANTITY NEGOTIATION =====
H --> AB["Can you supply [X] instead of [Y]?"]
AB --> AC{Seller Response}
AC -->|"Yes, updated to [X]"| AD{Buyer Response}
AC -->|"Only [Y] available"| AD
AD -->|Accept| M
AD -->|Cancel| N

%% ===== PICKUP / DELIVERY TERMS =====
I --> AE["I will arrange pickup"]
AE --> AF{Seller Response}
AF -->|"Ready for pickup at [Address]"| AG{Buyer Response}
AF -->|"Only delivery available"| AG
AG -->|Accept| M
AG -->|Cancel| N

I --> AH["Can you deliver to my address?"]
AH --> AI{Seller Response}
AI -->|"Delivery possible"| AJ{Buyer Response}
AI -->|"Only pickup allowed"| AJ
AJ -->|Accept| M
AJ -->|Cancel| N

I --> AK["Can we change the [pickup/delivery] address?"]
AK --> AL{Seller/Buyer Response}
AL -->|"Yes, update address"| AM{Seller/Buyer Response}
AL -->|"No, original address only"| AN{Seller/Buyer Response}
AM -->|Accept| M
AM -->|Cancel| N
AN -->|Accept| M
AN -->|Cancel| N

I --> AO["Can we reschedule this pickup/delivery to [new date]?"]
AO --> AP{Seller/Buyer Response}
AP -->|"Confirmed new pickup date"| AQ{Buyer Response}
AP -->|"Date cannot be changed"| AR{Buyer Response}
AQ -->|Accept Offer| M
AQ -->|Cancel Negotiation| N
AR -->|Accept Offer| M
AR -->|Cancel Negotiation| N

%% ===== QUALITY / WEATHER / HOLD OPTIONS =====
J --> AW["Please confirm if quality certification is available"]
AW --> AX{Buyer Response}
AX -->|"Only on-site check allowed"| AY{Seller Response}
AX -->|"Report after pickup inspection"| AY
AY -->|Accept Terms| M
AY -->|Cancel Negotiation| N

J --> AZ["There's a weather alert. Can we delay pickup to [date]?"]
AZ --> BA{Seller/Buyer Response}
BA -->|"Pickup delayed to [date] due to weather"| BB{Seller/Buyer Response}
BA -->|"Delay not possible"| BC{Seller/Buyer Response}
BB -->|Accept New Date| M
BB -->|Cancel Negotiation| N
BC -->|Accept Offer| M
BC -->|Cancel Negotiation| N

%% ===== FINALIZATION =====
M --> BD["System: Shall we confirm the order?"]
BD --> BE[Buyer pays 50% upfront if applicable]
BE --> BF[Order Confirmed]
BF --> BG[Timestamped Logs]
BG --> BH[Notifications Sent]

%% ===== POST ORDER CHAT OPTIONS (VISIBLE ONLY AFTER CONFIRMATION) =====
BH --> BI["Order Confirmed - Post Chat Options Available"]

subgraph "Post Order Chat Options (Visible Only After Order Confirmation)"
    BI --> CJ["Chat Options Visible"]
    CJ --> CK["Request Change: Pickup/Delivery Date/Time"]
    CJ --> CL["Request Change: Pickup/Delivery Address"]

    %% Pickup/Delivery Date Change Flow
    CK --> CM{"Choose Action for Date"}
    CM -- Propose New Date --> CN["Enter New Date"]
    CM -- Accept Current Date --> CO["Exit Flow"]
    CM -- Cancel Request --> CP["Exit Flow"]
    CN --> CQ{"Other Party Response"}
    CQ -- Accept --> CR["Update Order with New Date/Time"]
    CQ -- Cancel --> CP
    CQ -- Counter --> CS["Allow Propose New Date Again (Max 3 times)"]
    CS --> CN

    %% Address Change Flow
    CL --> CT{"Choose Action for Address"}
    CT -- Submit New Address --> CU["Enter New Address"]
    CT -- Cancel Request --> CV["Exit Flow"]
    CU --> CW{"Other Party Response"}
    CW -- Request Update --> CX["Buyer/Seller Updates Address"]
    CW -- Accept --> CY["Update Order with New Address"]
    CW -- Cancel --> CZ["Keep Original Address"]
    CX --> DA{"Final Response After Update"}
    DA -- Accept --> CY
    DA -- Cancel --> CZ
end

%% ===== SYSTEM RULES =====
subgraph "System Rules"
    BI1[Max 4 negotiation rounds]
    BJ[Auto-expire after 48h]
    BK[No free-text input]
    BL[All actions timestamped]
end

%% ===== STYLES =====
style M fill:#D4EDDA,stroke:#28A745,stroke-width:2px
style N fill:#F8D7DA,stroke:#C82333,stroke-width:2px
style W fill:#F8D7DA,stroke:#C82333,stroke-width:2px
style BF fill:#D4EDDA,stroke:#28A745,stroke-width:2px
style BG fill:#D4EDDA,stroke:#28A745,stroke-width:2px
style BH fill:#D4EDDA,stroke:#28A745,stroke-width:2px
style BD fill:#D4EDDA,stroke:#28A745,stroke-width:2px
style BE fill:#D4EDDA,stroke:#28A745,stroke-width:2px
style BI1 fill:#E2E3E5,stroke:#6C757D,stroke-width:2px
style BJ fill:#E2E3E5,stroke:#6C757D,stroke-width:2px
style BK fill:#E2E3E5,stroke:#6C757D,stroke-width:2px
style BL fill:#E2E3E5,stroke:#6C757D,stroke-width:2px

classDef negotiation fill:#FFFACD,stroke:#FFC107,stroke-width:2px;
class G,G1,G2,G3,G4,G5,O,P,Q,R,S,T,U,V,X,Y,Z,AA negotiation;
