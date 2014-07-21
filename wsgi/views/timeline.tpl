%#list of currents logs
%include shared/header.tpl header=page,logged=1
<div id="main">
         <table id="twtable" class="sortable" cellspacing="0"
               summary="Last logs">
        <tr>
             <th scope="col" abbr="timeline" class="nobackground">timeline</th>
             <th scope="col" abbr="@when">Timestamp</th>
             <th scope="col" abbr="tag">Tag</th>
             <th scope="col" abbr="@who">Host Ip</th>
           </tr>

%import time
	%for log in loglist:
               %thetime = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(log['timestamp']))
		 <tr id='tweetrow'>
                <td class='when' colspan='2'>{{thetime}}</td>
                <td class='searchtag'> {{log['tag']}}</td>
                <td class='who'> {{log['host']}}</td>
                </tr>
        %end

</table>
</div>

