import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"  # Change to your EC2 IP if deployed

st.set_page_config(
    page_title="Insurance Premium Predictor - Bangladesh",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Insurance Premium Category Predictor")
st.markdown("### For Bangladesh Residents")
st.markdown("Enter your details below to get an insurance premium prediction:")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("📅 Age", min_value=1, max_value=119, value=30, help="Your age in years")
    weight = st.number_input("⚖️ Weight (kg)", min_value=1.0, max_value=300.0, value=65.0, help="Your weight in kilograms")
    height = st.number_input("📏 Height (m)", min_value=0.5, max_value=2.5, value=1.7, help="Your height in meters")
    income_lpa = st.number_input("💰 Annual Income (Lakh BDT)", min_value=0.1, max_value=1000.0, value=10.0, help="Your annual income in lakhs (1 lakh = 100,000 BDT)")

with col2:
    smoker = st.selectbox("🚬 Are you a smoker?", options=[False, True], format_func=lambda x: "Yes" if x else "No")
    
    # Bangladesh cities grouped by tier
    tier_1_cities = ["Dhaka", "Chittagong", "Gazipur", "Narayanganj", "Khulna", "Rajshahi", "Sylhet", "Rangpur"]
    tier_2_cities = [
        "Mymensingh", "Barishal", "Comilla", "Narsingdi", "Jessore", "Bogra", "Cox's Bazar", "Dinajpur",
        "Nawabganj", "Tangail", "Sirajganj", "Pabna", "Naogaon", "Faridpur", "Brahmanbaria", "Kushtia",
        "Satkhira", "Madaripur", "Gopalganj", "Manikganj", "Munshiganj", "Noakhali", "Feni", "Lakshmipur",
        "Chandpur", "Habiganj", "Maulvibazar", "Sunamganj", "Netrokona", "Sherpur", "Jamalpur", "Kishoreganj",
        "Thakurgaon", "Panchagarh", "Nilphamari", "Lalmonirhat", "Kurigram", "Gaibandha", "Joypurhat",
        "Chapai Nawabganj", "Natore", "Rajbari", "Shariatpur", "Magura", "Jhenaidah", "Meherpur", "Chuadanga",
        "Bagerhat", "Pirojpur", "Jhalokati", "Barguna", "Patuakhali", "Bhola", "Bandarban", "Rangamati",
        "Khagrachari"
    ]
    all_cities = tier_1_cities + tier_2_cities + ["Other"]
    
    city = st.selectbox("🏙️ City", options=all_cities, index=0, help="Select your city from Bangladesh")
    
    occupation = st.selectbox(
        "💼 Occupation",
        ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'],
        format_func=lambda x: x.replace('_', ' ').title()
    )

st.markdown("---")

if st.button("🔮 Predict Premium Category", type="primary", use_container_width=True):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    with st.spinner("Analyzing your information..."):
        try:
            response = requests.post(API_URL, json=input_data, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                
                if "predicted_category" in result:
                    prediction = result["predicted_category"]
                    
                    # Display prediction with appropriate color
                    if prediction == "High":
                        st.error(f"## ⚠️ Predicted Premium Category: **{prediction}**")
                        st.info("💡 High premium suggests you might have higher risk factors. Consider healthier lifestyle choices.")
                    elif prediction == "Medium":
                        st.warning(f"## 📊 Predicted Premium Category: **{prediction}**")
                        st.info("💡 Medium premium indicates moderate risk. Maintaining healthy habits could help lower your premium.")
                    else:
                        st.success(f"## ✅ Predicted Premium Category: **{prediction}**")
                        st.info("💡 Low premium suggests you're in a lower risk category. Great job maintaining a healthy lifestyle!")
                    
                    if "confidence" in result:
                        st.write(f"📈 **Confidence Score:** {result['confidence']*100:.1f}%")
                    
                    if "class_probabilities" in result:
                        with st.expander("📊 Detailed Probability Breakdown"):
                            probs = result["class_probabilities"]
                            for category, prob in probs.items():
                                st.progress(prob, text=f"{category}: {prob*100:.1f}%")
                
                elif "detail" in result:
                    st.error(f"Error: {result['detail']}")
                else:
                    st.write("Response:", result)
                    
            else:
                st.error(f"❌ API Error: {response.status_code}")
                try:
                    error_detail = response.json()
                    st.write(error_detail)
                except:
                    st.write(response.text)

        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to the FastAPI server. Make sure it's running on port 8000.")
            st.info("To start the server, run: `uvicorn app:app --reload --host 0.0.0.0 --port 8000`")
        except requests.exceptions.Timeout:
            st.error("⏰ Request timed out. Please try again.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

st.markdown("---")
st.caption("© 2024 Insurance Premium Predictor - Powered by Machine Learning | For Bangladesh Residents")