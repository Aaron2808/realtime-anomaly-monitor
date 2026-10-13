package com.realtimeanomaly.api;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Reading {
    
    String timestamp = "";

    @JsonProperty("machine_id")
    String machineId = "";
    
    String metric = "";
    float value = 0;

    public Reading(){
        
    }

    public void setTimestamp(String timestamp){
        this.timestamp = timestamp;
    }

     public void setMachineId(String machineId){
        this.machineId = machineId;
    }

     public void setMetric(String metric){
        this.metric = metric;
    }

     public void setValue(float value){
        this.value = value;
    }



    public String getTimestamp(){
        return this.timestamp;
    }

    public String getMachineId(){
        return this.machineId;
    }

    public String getMetric(){
        return this.metric;
    }
    
    public float getValue(){
        return this.value;
    }
}
