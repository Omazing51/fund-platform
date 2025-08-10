import axios from "axios";

const API_URL = "http://localhost:8000/subscriptions";

export async function getAllSubscription() {
  const response = await axios.get(API_URL);
  return response.data.data;
}

export async function getSubscriptionById(id) {
  const response = await axios.get(`${API_URL}/${id}`);
  return response.data.data;
}

export async function deleteSubscription(fundId) {
  const response = await axios.delete(API_URL, {
    data: { FundId: fundId } 
  });
  return response.data;
}

export async function createSubscription(FundId, NotificationMethod) {
  const response = await axios.post(API_URL, {
    FundId: String(FundId),       
    NotificationMethod            
  }, {
    headers: { "Content-Type": "application/json" }
  });
  return response.data;
}
