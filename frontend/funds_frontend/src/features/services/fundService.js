import axios from "axios";

const API_URL = "http://localhost:8000/funds"; 

export async function getAllFunds() {
  const response = await axios.get(API_URL);
  return response.data.data; 
}

export async function getFundById(id) {
  const response = await axios.get(`${API_URL}/${id}`);
  return response.data.data;
}

