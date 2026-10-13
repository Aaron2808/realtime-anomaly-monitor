package com.realtimeanomaly.api;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;


@RestController 
public class ReadingController {
    
    @PostMapping("/readings")
    public void postReading(@RequestBody Reading reading) {
        
        System.out.println("Machine: " + reading.getMachineId()
            + " Metric: " + reading.getMetric()
            + " Value: " + reading.getValue());
    }
    

}
