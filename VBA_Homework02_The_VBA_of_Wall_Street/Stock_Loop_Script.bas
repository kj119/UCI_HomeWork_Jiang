Attribute VB_Name = "Module2"
Sub StockLoop():

    Dim previousTicker As String
    Dim openPrice As Double
    Dim outputRow As Integer
    Dim yearlyDiff As Double
    
    lastRow = Cells(Rows.Count, 1).End(xlUp).row
    previousTicker = ""
    openPrice = 0
    outputRow = 1
    
    For i = 2 To lastRow
    
        currentTicker = Cells(i, 1).Value
        
        If currentTicker <> previousTicker And openPrice = 0 Then
        
            'adds column headers
            Cells(1, 9).Value = "Ticker"
            
            Cells(1, 10).Value = "Yearly Change"
            
            Cells(1, 11).Value = "Percent Change"
            
            Cells(1, 12).Value = "Total Stock Volume"
            
            'handle first instance of ticker
            openPrice = Cells(i, 3).Value
            
            'handle first instance of volume for the first ticker
            currentVolume = Cells(i, 7).Value
            
        ElseIf currentTicker = previousTicker Then
        
            finalVolume = currentVolume + Cells(i, 7).Value
            
            'update current overall volume per ticker
            currentVolume = finalVolume
        
        ElseIf currentTicker <> previousTicker Then
        
            'found solution
            
            closePrice = Cells(i - 1, 6).Value
            
            yearlyDiff = closePrice - openPrice
            
            percentChange = ((closePrice - openPrice) / openPrice)
            
            outputRow = outputRow + 1
            
            Cells(outputRow, 9).Value = previousTicker
            
            Cells(outputRow, 10).Value = yearlyDiff
            
            Cells(outputRow, 11).Value = Format(percentChange, "Percent")
            
            Cells(outputRow, 12).Value = currentVolume
            
            currentVolume = Cells(i, 7).Value
            
            openPrice = Cells(i, 3).Value
            
        End If
        
        'update previous ticker
        previousTicker = currentTicker
        
        'change color of percentChange column
        If Cells(outputRow, 10).Value > 0 Then
        
           Cells(1, 10).Interior.ColorIndex = 2
           
           Cells(outputRow, 10).Interior.ColorIndex = 4
           
        Else
        
            Cells(outputRow, 10).Interior.ColorIndex = 3
            
        End If
        
    Next i
    
    'last ticker output
    yearlyDiff = Cells(lastRow, 6).Value - openPrice
    
    percentChange = ((Cells(lastRow, 6).Value - openPrice) / openPrice)
    
    outputRow = outputRow + 1
    
    Cells(outputRow, 9).Value = previousTicker
    
    Cells(outputRow, 10).Value = yearlyDiff
    
    Cells(outputRow, 11).Value = Format(percentChange, "Percent")
    
    Cells(outputRow, 12).Value = currentVolume
    
    If Cells(outputRow, 10).Value > 0 Then
    
        Cells(outputRow, 10).Interior.ColorIndex = 4
        
    Else
    
        Cells(outputRow, 10).Interior.ColorIndex = 3
        
    End If
    
    'Challenge question
    newLastRow = Cells(Rows.Count, 11).End(xlUp).row
    Dim max As Double
    Dim min As Double
    Dim maxVolume As Variant
    Dim volume As Variant
    
    max = 0
    min = 0
    maxVolume = 0
    
    For j = 2 To newLastRow
    
        volume = Cells(j, 12).Value
        
        'checks max percentage change
        If Cells(j, 11).Value > max Then
        
            max = Cells(j, 11).Value
            maxTicker = Cells(j, 9).Value
            
        End If
            
        'checks min percentage change
        If Cells(j, 11).Value < min Then
        
            min = Cells(j, 11).Value
            minTicker = Cells(j, 9).Value
            
        End If
            
        'checks max stock volume
        If volume > maxVolume Then
        
            maxVolume = volume
            maxVolumeTicker = Cells(j, 9).Value
            
        End If
        
    Next j
    
    'solutions output
    Cells(2, 16).Value = Format(max, "Percent")
    Cells(2, 15).Value = maxTicker
    Cells(3, 16).Value = Format(min, "Percent")
    Cells(3, 15).Value = minTicker
    Cells(4, 16).Value = maxVolume
    Cells(4, 15).Value = maxVolumeTicker
    
    'column/row headers
    Cells(1, 15).Value = "Ticker"
    Cells(1, 16).Value = "Value"
    Cells(2, 14).Value = "Greatest % Increase"
    Cells(3, 14).Value = "Greatest % Decrease"
    Cells(4, 14).Value = "Greatest Total Volume"

End Sub
